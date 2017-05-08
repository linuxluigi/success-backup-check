install

```bash
    pip3 install git+git://github.com/linuxluigi/success-backup-check.git
```

usage
```bash
    success-backup-check
```

/etc/success_backup_check.conf

[Mail]
From = from@example.com
To = to@example.com
ApiKey = YourSendGridApiKey

[Time]
days = 3

[BackupDirs]
VeryImportant = /path/to/backup/
VeryImportentToo = /another/path/Backup/
