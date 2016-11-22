from success_backup_check.read_config import readConfig
from success_backup_check.check_backup import check_backup
from  success_backup_check.send_mail import sendMail

def start():
    '''
    start the programm
    Returns:

    '''

    # load config
    conf = readConfig()

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