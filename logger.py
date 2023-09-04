import logging


class Logger:
    logger = None
    date_format = "%Y-%m-%d %H:%M:%S"

    @classmethod
    def initialize(cls, name, log_file=None, log_level=logging.DEBUG):
        cls.logger = logging.getLogger(name)
        cls.logger.setLevel(log_level)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt=cls.date_format,
        )

        if log_file:
            file_handler = logging.FileHandler(log_file, mode="a")
            file_handler.setFormatter(formatter)
            cls.logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        cls.logger.addHandler(console_handler)

    @classmethod
    def debug(cls, message):
        cls.logger.debug(message)

    @classmethod
    def info(cls, message):
        cls.logger.info(message)

    @classmethod
    def warning(cls, message):
        cls.logger.warning(message)

    @classmethod
    def error(cls, message):
        cls.logger.error(message)

    @classmethod
    def critical(cls, message):
        cls.logger.critical(message)
