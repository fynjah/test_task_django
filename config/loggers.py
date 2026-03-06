import os
from django.utils import timezone

now = timezone.now()
path = "files/logs/server"
path += f"/{now.year}"

if not os.path.exists(path):
    os.mkdir(path)

path += f"/{now.month}"
if not os.path.exists(path):
    os.mkdir(path)

path += f"/{now.day}.log"
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {"format": "LOG_%(levelname)-2s %(name)-12s: %(message)s;"},
        "file": {"format": "%(asctime)s %(levelname)-2s %(message)s"},
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "console"},
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "formatter": "file",
            "filename": path,
        },
    },
    "loggers": {"": {"level": "INFO", "handlers": ["console", "file"]}},
}
