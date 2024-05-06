import logging
import logging.config
import logging.handlers

from opentelemetry.instrumentation.logging import LoggingInstrumentor

from .config.logformat import LogFormat


class BaseLog:
    def __init__(self, logger_name: str):
        LoggingInstrumentor().instrument()

        self.logger = logging.getLogger(logger_name)
        logging.config.dictConfig(LogFormat.config())
