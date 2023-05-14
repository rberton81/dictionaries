import logging


def get_logger(name, filename=None, level=None):
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter()
    if filename:
        handler = logging.FileHandler(filename=filename)
    handler.setFormatter(formatter)
    if level is not None:
        logger.setLevel(level)
    else:
        logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger
