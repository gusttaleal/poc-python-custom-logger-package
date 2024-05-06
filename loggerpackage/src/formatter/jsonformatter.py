import datetime as dt
import json
import logging

LOG_RECORDS_BUILTIN_ATTRS = {
    "args",
}


class JSONFormatter(logging.Formatter):
    def __init__(
            self,
            *,
            formart_keys: dict[str, object] | None = None,
    ):
        super().__init__()
        self.format_keys = formart_keys if formart_keys is not None else {}

    def format(self, record: logging.LogRecord) -> str:
        message = self._prepare_log_dict(record)
        return json.dumps(message, default=str)

    def _prepare_log_dict(self, record: logging.LogRecord):
        message = self._format_message(self.format_keys, record)

        if record.exc_info is not None:
            message["ExceptionInfo"] = self.formatStack(record.exc_info)
        if record.stack_info is not None:
            message["StackInfo"] = self.formatStack(record.stack_info)

        for key, value in record.__dict__.items():
            if key not in LOG_RECORDS_BUILTIN_ATTRS:
                message[key] = value

        return message

    def _format_message(self, _input: dict, record: logging.LogRecord) -> dict:
        output = {}
        for key, value in _input.items():
            if not isinstance(value, str):
                output[key] = self._format_message(value, record)
                continue
            if key == "Timestamp":
                output[key] = self._format_time(record.created)
            else:
                output[key] = getattr(record, value)
        return output

    def _format_time(self, time: float) -> str:
        return dt.datetime.fromtimestamp(time, tz=dt.timezone.utc).isoformat()
