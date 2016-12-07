install

```bash
    pip3 install git+git://github.com/linuxluigi/success-backup-check.git
```

usage
```bash
    success-backup-check
```

/etc/success_backup_check.conf

[Server]
Host: smtp.example.com
Port: 465
Username: sou@example.com
Password: password

[Mail]
From = from@example.com
To = to@example.com

[Time]
days = 3

[BackupDirs]
VeryImportant = /path/to/backup/
VeryImportentToo = /another/path/Backup/