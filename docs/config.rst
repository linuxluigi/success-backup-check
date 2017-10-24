======
Config
======

Complete Example::

    [Mail]
    From = from@example.com
    To = to@example.com
    ApiKey = YourSendGridApiKey

    [Time]
    days = 3

    [Server]
    ArchivDir = /srv/backup/daily_backup/
    mode = active
    file_typ = MDB

    [BackupDirs]
    MyDatabaseDir = /home/user/daily-db
    UserWork = /home/user/done/work

    [Logging]
    log_level = WARNING
    log_file = /var/log/succes_backup_check.log

Mail
^^^^

Mails are send via https://sendgrid.com and need a ``From`` & ``To`` email address and also the sendgrid api key via ``ApiKey``.::

    [Mail]
    From = from@example.com
    To = to@example.com
    ApiKey = YourSendGridApiKey

Time
^^^^

Right now there is the section ``[Time]`` just one option. How many ``days`` one folder can be outdated.::

    [Time]
    days = 3

Server
^^^^^^

``[Server]`` is for selecting the master backup path on the server & set the server ``mode``.

- ``ArchivDir`` is the master path in witch the backups are will be save to.

- ``mode`` has 2 values ``active`` -> move the files from original path to the backup folder & ``passive`` -> just check if
  the active server has done the work right. The default value is ``passive``

- `file_typ` set the typ of files witch should be backup. Examples all databases with the ending ``MDB``.

.. code::

    [Server]
    ArchivDir = /srv/backup/daily_backup/
    mode = active
    file_typ = MDB

BackupDirs
^^^^^^^^^^

The ``[BackupDirs]`` Section set witch directory should be backed up. Every entry is a new directory. On the left side
is the name of the new directory on the backup server & on the right side ios the full path of the to back up directory::

    [BackupDirs]
    MyDatabaseDir = /home/user/daily-db
    UserWork = /home/user/done/work

Logging
^^^^^^^

``[Logging]`` is for selecting the ``log_level`` (WARNING, INFO, DEBUG) & where to save to the ``log_file``::

    [Logging]
    log_level = WARNING
    log_file = /var/log/succes_backup_check.log
