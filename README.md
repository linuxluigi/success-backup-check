# Succes-Backup-Check

[![Build Status](https://travis-ci.org/linuxluigi/success-backup-check.svg?branch=master)](https://travis-ci.org/linuxluigi/success-backup-check)
[![Coverage Status](https://coveralls.io/repos/github/linuxluigi/success-backup-check/badge.svg?branch=master)](https://coveralls.io/github/linuxluigi/success-backup-check?branch=master)

Move user files on a server from a place where the user has write rights & move it to an archive or backup folder, where
to user has no read or write access.

A use case example: Daily backup of a point-of-sale database. So that every point-of-sale device has only the current
database in the storage. The 2 server check in the operation when was the last backup & send an email if the current
database on the server is to old.

![Overview](docs/_static/Overview.png "function overview")


## Online Documentation

http://success-backup-check.readthedocs.io/en/latest/

# Quickstart

## Install

### Requirements

- https://www.smartmontools.org for hardware tests

Debian / Ubuntu::

    $ sudo apt-get install smartmontools python3-pip git

Mac - Brew::

    $ brew install smartmontools
    
### Install

Install it from online resource directly.

    $ sudo python3 -m pip install git+git://github.com/linuxluigi/success-backup-check.git
    

Or download the archive from git & install it from there. 

    $ git clone git@github.com:linuxluigi/success-backup-check.git
    $ cd success-backup-check
    $ python setup.py install --user

## Usage

To run the program run:

    $ success-backup-check

Or an example in crontab. (change your Python version)

    $ python3 /usr/local/lib/python3.5/dist-packages/success_backup_check/__main__.py

## Config Example

Quick Example, for detail instruction read the documentation.
http://success-backup-check.readthedocs.io/en/latest/config.html

File: ```/etc/success_backup_check.conf```

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
