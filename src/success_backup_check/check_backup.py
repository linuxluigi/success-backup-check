import os
import logging
from datetime import datetime, timedelta


def get_directory_age(directory):
    # var for the newest folder in directory
    newest_item = None

    # search for the newest backup in directory
    try:
        for sub_dir in os.listdir(directory):

            # convert the folder name into a datetime object
            try:
                sub_dir_datetime = datetime.strptime(sub_dir, "%Y-%m-%d_%H:%M")
            except ValueError:
                sub_dir_datetime = None

            # if the folder was converted into a datetime object, check for the newest one
            if sub_dir_datetime:

                if not newest_item:
                    newest_item = sub_dir_datetime

                if sub_dir_datetime > newest_item:
                    newest_item = sub_dir_datetime
    except FileNotFoundError as e:
        return e

    return newest_item


def check_backup(directory, days) -> bool:
    """
    Check a Directory if the last modify date is older than n days
        Args:
            directory: Directory witch will be checked
            days: modify time in days

        Returns: False --> the dir is out of date
                 True --> everything is fine
    """

    logging.debug('check %s if up to date' % directory)

    newest_item = get_directory_age(directory)

    # no directory was backup
    if newest_item is None:
        logging.warning('there is no backup @ %s' % directory)
        return False

    # current time minus the day delay
    max_backup_age = datetime.now() - timedelta(days=int(days))

    if max_backup_age > newest_item:
        logging.warning('%s is outdated' % directory)
        return False
    else:
        logging.info('%s is fine' % directory)
        return True
