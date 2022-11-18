import logging

_log_format = f'%(asctime)s [%(levelname)s] %(message)s'


def get_file_handler():
    file_handler = logging.FileHandler('logs/api.log')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_file_handler())
    return logger

