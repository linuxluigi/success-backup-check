import argparse
from success_backup_check import __version__, read_config, set_logging, hdd_smart_test, check_backup, \
    archiv_files, send_mail
from os import path, makedirs
import logging


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

        backup_path = path.join(conf['Server']['ArchivDir'], key)

        # check if backup_path exists & create it when necessary
        if not path.exists(backup_path):
            makedirs(backup_path)

        # check if backup_path is a directory
        if not path.isdir(backup_path) & path.exists(backup_path):
            waring_text = '%s no directory or not exists' % backup_path
            logging.warning(waring_text)
            send_mail.send_simple_message(
                conf,
                waring_text,
                waring_text)

        else:
            # move the backup files
            if conf['Server']['mode'] == "active":
                archiv_files.archiv_files(
                    value,
                    backup_path,
                    conf['Server']['file_typ']
                )

            # check if the backup directory is outdated
            if not check_backup.check_backup(backup_path, conf['Time']['days']):
                msg = 'Backup "%s" is out of date, please check if the backup run correctly!' % key

                send_mail.send_simple_message(
                    conf,
                    "Warning: Backup is out of Date!",
                    msg)

                logging.warning("Mail was send reason: %s is out of date" % key)

    # HDD SMART test
    hdd_smart_test.main(conf)


if __name__ == '__main__':
    main()
