from pathlib import Path
import configparser

def readConfig():
    '''
    Read the config '/etc/success_backup_check.conf' and return it's content
    Returns:
        Confgig content

    '''
    ConfigPath = "/etc/success_backup_check.conf"
    configFile = Path(ConfigPath)

    # check if config exists
    if configFile.is_file() == False:
        return "Missing config '%s", ConfigPath

    # read config
    Config = configparser.ConfigParser()
    Config.read(ConfigPath)

    return Config

