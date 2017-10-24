import argparse
from success_backup_check import __version__, read_config, set_logging, hdd_smart_test, check_backup, send_mail, \
    archiv_files
from os import path


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

    # backup files
    backup_dirs = dict(conf.items('BackupDirs'))

    for key, value in backup_dirs.items():
        if check_backup.check_backup(value, conf['Time']['days']):
            msg = 'Backup "%s" is out of date, please check if the backup run correctly!' % key

            send_mail.send_mail(
                conf['Mail']['From'],
                conf['Mail']['To'],
                msg,
                "Warning: Backup is out of Date!",
                conf['Mail']['ApiKey']
            )
            print("mail was send for %s" % key)

        if conf['Server']['mode'] == "active":
            archiv_files.archiv_files(
                value,
                path.join(conf['Server']['ArchivDir'], key),
                conf['Server']['file_typ']
        )

    # HDD SMART test
    hdd_smart_test.main(conf)


if __name__ == '__main__':
    main()
