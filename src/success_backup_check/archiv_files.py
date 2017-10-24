import datetime
import os.path
import shutil
import logging

from os import mkdir


def search_dir(path, extension):
    """
       extension with leading point, for example: ".MDB"

    Args:
        path:
        extension:
    """
    for root, dirs, filenames in os.walk(path):
        for filename in filenames:
            if os.path.splitext(filename)[-1] == extension:
                yield os.path.join(root, filename)


def archiv_files(directory, archive_dir, extension="MDB"):
    """
    Move Files with the default ending extension from dir to archive_dir
    Args:
        directory: original dir, where the database is right now
        archive_dir: archiv dir, werhe the database will move to
        extension: file ending name, default "MDB"

    Returns:

    """
    new_backups = list(search_dir(directory, '.' + extension))

    if not new_backups:
        return False

    if not os.path.exists(archive_dir):
        mkdir(archive_dir)

    new_backup_dir = os.path.join(archive_dir, datetime.datetime.now().strftime("%Y-%m-%d_%H:%M"))
    mkdir(new_backup_dir)

    for file in new_backups:
        shutil.move(
            file,
            os.path.join(new_backup_dir, os.path.basename(file))
        )

    return True
