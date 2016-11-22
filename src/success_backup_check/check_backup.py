import os.path, time

def check_backup(dir, days):
    '''
    Check a Directory if the last modify date is older than n days
    Args:
        dir: Directory wich will be checked
        days: modify time in days

    Returns: True --> the dir is out of date
             False --> everything is fine

    '''
    timeMaxDelay = time.time() - 86400 * float(days)
    if (os.path.getmtime(dir) < timeMaxDelay):
        return True
    else:
        return False




