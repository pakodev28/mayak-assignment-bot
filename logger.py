import logging
from logging.handlers import RotatingFileHandler


def get_file_handler():
    file_handler = RotatingFileHandler(
        "mayak_bot.log", maxBytes=50000000, backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s,%(levelname)s,%(message)s,%(name)s")
    )
    return file_handler


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_file_handler())
    return logger
