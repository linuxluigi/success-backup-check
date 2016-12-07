from os import path

from success_backup_check.read_config import readConfig
from success_backup_check.check_backup import check_backup
from success_backup_check.send_mail import sendMail
from success_backup_check.archiv_files import archiv_files

def start():
    '''
    start the programm
    Returns:

    '''

    print("read config")
    # load config
    conf = readConfig()

    print("test every backup dir")
    # test every backup dir
    BackupDirs = dict(conf.items('BackupDirs'))

    for key, value in BackupDirs.items():
        if (check_backup(value, conf['Time']['days'])):
            msg = 'Backup "%s" is out of date, please check if the backup run correctly!' % (key)

            sendMail(
                conf['Mail']['From'],
                conf['Mail']['To'],
                msg,
                "Warning: Backup is out of Date!",
                conf['Server']['Username'],
                conf['Server']['Password'],
                conf['Server']['Host'],
                conf['Server']['Port']
            )
            print("mail was send for %s" % key)
        archiv_files(
            value,
            path.join(conf['Server']['ArchivDir'], key)
        )
