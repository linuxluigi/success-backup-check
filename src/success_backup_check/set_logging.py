import logging


def set_logging(logging_level, log_file):
    """
    Setup logging config to log into terminal & log file.
    Just execute set_logging(logging_level, log_file) and start of the script & every time when logging will use this
    config.

    Args:
        logging_level: string "DEBUG", "INFO" or "WARNING"
        log_file: full path of the log file example: "/var/log/mylog.log"
    """

    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                        filename=log_file,
                        datefmt='%m/%d/%Y %H:%M:%S',
                        level=get_logging_level(logging_level))

    stderrLogger = logging.StreamHandler()
    stderrLogger.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
    logging.getLogger().addHandler(stderrLogger)

    logging.debug('logging is setup')


def set_logging_minimal(logging_level):
    """
    Set logging minimal logging, just writing log to console without saving it into a file.
    Args:
        logging_level: string "DEBUG", "INFO" or "WARNING"
    """
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%m/%d/%Y %H:%M:%S',
                        level=get_logging_level(logging_level))

    logging.debug('minimal logging is setup')


def get_logging_level(logging_level):
    """
    Change string into logging level.
    Example "DEBUG" -> logging.DEBUG

    Returns:
        object: logging level
                "DEBUG" -> logging.DEBUG
                "INFO" -> logging.INFO
                "WARNING" -> logging.WARNING
                default -> logging.WARNING
    """

    switcher = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
    }

    return switcher.get(logging_level, logging.WARNING)


def main(logging_level="WARNING", log_file=None):
    if log_file:
        set_logging(logging_level, log_file)
    else:
        set_logging_minimal(logging_level)


if __name__ == '__main__':
    main()
