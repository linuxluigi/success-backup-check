from pathlib import Path
import configparser
import logging


def main(config_path):
    """
    Read the config from the file at config_path and return it's content
    Args:
        config_path (object): str complete path of the config file

    Returns:
        config content

    """
    config_file = Path(config_path)

    # check if config exists
    if not config_file.is_file():
        error_msg = ('Config file is missing @ %s' % config_path)
        logging.warning(error_msg)
        return error_msg

    # read config
    config = configparser.ConfigParser()
    config.read(config_path)

    return config


if __name__ == '__main__':
    main()
