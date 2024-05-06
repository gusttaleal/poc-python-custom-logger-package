class LogFormat:
    @classmethod
    def config(cls):
        return {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "simple": {
                    "format": "%(levelname)s"
                },
                # "json": {
                #     "()": "loggerpackage.src.formatter.jsonformatter.JSONFormatter",
                #     "format_keys": {
                #         "timestamp": "timestamp",
                #         "traceId": "otelTraceID",
                #         "spanID": "otelSpanID",
                #     }
                # }
            },
            "handlers": {
                "stdout": {
                    "class": "logging.StreamHandler",
                    "level": "INFO",
                    "formatter": "json",
                    "stream": "ext://sys.stdout"
                }
            },
            "loggers": {
                "root": {
                    "level": "INFO",
                    "handlers": [
                        "stdout"
                    ]
                }
            }
        }
