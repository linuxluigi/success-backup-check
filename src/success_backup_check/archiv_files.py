import datetime
import os.path
import shutil

from os import mkdir


def search_dir(path, extension):
    """
       extension with leading point, for example: ".MDB"
    """
    for root, dirs, filenames in os.walk(path):
        for filename in filenames:
            if os.path.splitext(filename)[-1] == extension:
                yield os.path.join(root, filename)


def archiv_files(dir, archiv_dir):
    """
    Move Database Files with the Ending MDB from dir to archiv_dir
    Args:
        dir: original dir, where the database is right now
        archiv_dir: archiv dir, werhe the database will move to

    Returns:

    """
    new_backups = list(search_dir(dir, '.MDB'))

    if not new_backups:
        return False

    if not os.path.exists(archiv_dir):
        mkdir(archiv_dir)

    new_backup_dir = os.path.join(archiv_dir, datetime.datetime.now().strftime("%Y-%m-%d_%H:%M"))
    mkdir(new_backup_dir)

    for file in new_backups:
        shutil.move(
            file,
            os.path.join(new_backup_dir, os.path.basename(file))
        )

    return True
