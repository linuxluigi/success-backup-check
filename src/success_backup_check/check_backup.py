import os.path
import time
import logging


def check_backup(directory, days):
    """
    Check a Directory if the last modify date is older than n days
        Args:
            directory: Directory witch will be checked
            days: modify time in days

        Returns: True --> the dir is out of date
                 False --> everything is fine
    """

    # convert days into seconds
    time_max_delay = time.time() - 86400 * float(days)

    if os.path.getmtime(directory) < time_max_delay:
        logging.warning('%s is outdated' % directory)
        return True
    else:
        logging.info('%s is fine' % directory)
        return False
