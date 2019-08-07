=========================
Installation instructions
=========================

Requirements
------------

- Python 3.x
- https://www.smartmontools.org for hardware tests

Linux
^^^^^

Debian / Ubuntu::

    $ sudo apt-get install smartmontools python3-pip

Mac
^^^

Brew::

    $ brew install smartmontools

Install
-------

success-backup-check can be installed using pip::

    $ sudo python3 -m pip install git+git://github.com/linuxluigi/success-backup-check.git

This command will fetch the archive and its dependencies from the internet and
install them.

Or download it from git and execute::

    $ sudo apt-get install libffi-dev build-essential libssl-dev python3-dev
    $ git clone git@github.com:linuxluigi/success-backup-check.git
    $ cd success-backup-check
    $ python3 setup.py install --user

You might prefer to install it system-wide. In this case, skip the ``--user``
option and execute as superuser by prepending the command with ``sudo``.


Autoboot
--------

To start on boot enable the service::

    $ sudo systemctl daemon-reload
    $ sudo systemctl enable backup.service
    $ sudo systemctl start backup.service
    $ sudo systemctl status backup.service

Troubleshoot
------------

Only tested on linux & mac, I don't know this will work correctly on windows machines.

Windows users may find that these command will only works if typed from Python's
installation directory.

Some Linux distributions (e.g. Ubuntu) install Python without installing pip.
Please install it before. If you don't have root privileges, download the
get-pip.py script at https://bootstrap.pypa.io/get-pip.py and execute it as
``python get-pip.py --user``.
