import argparse

from success_backup_check import __version__, read_config, set_logging
from .telegram_bot import BotDaemon


def get_parser():
    """
    Creates a new argument parser.
    """
    parser = argparse.ArgumentParser('success-backup-check')

    version = '%(prog)s ' + __version__
    parser.add_argument('--version', '-v', action='version', version=version)

    parser.add_argument("--config",
                        dest="config_path",
                        default="/etc/success_backup_check.conf",
                        help="Path to config file")

    return parser


def main(args=None):
    """
    Main entry point

    Args:
        args : list
            A of arguments as if they were input in the command line. Leave it
            None to use sys.argv.
    """

    parser = get_parser()
    args = parser.parse_args(args)

    # setup minimal logging
    set_logging.main()

    # load config
    conf = read_config.main(args.config_path)

    # setup normal logging
    set_logging.main(logging_level=conf['Logging']['log_level'], log_file=conf['Logging']['log_file'])

    print('Success Backup Bot is starting :)')
    BotDaemon(conf)


if __name__ == '__main__':
    main()
