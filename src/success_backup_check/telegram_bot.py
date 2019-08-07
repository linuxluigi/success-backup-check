import logging
from os import path, makedirs

import requests
from telegram.ext import Updater, CommandHandler
import json

import subprocess

from success_backup_check import hdd_smart_test, check_backup, \
    archiv_files, send_mail
from success_backup_check.check_backup import get_directory_age


class BotDaemon:
    """
    Telegram Bot Daemon
    """

    def __init__(self, conf):
        self.conf = conf

        # setup telegram daemon
        self.updater = Updater(self.conf['TelegramBot']['bot'])
        self.job = self.updater.job_queue
        self.job_day = self.job.run_repeating(self.run_backup, interval=86400, first=0)  # run once a day

        # set bot commands to functions
        self.updater.dispatcher.add_handler(
            CommandHandler('help', self.help))
        self.updater.dispatcher.add_handler(
            CommandHandler('run_backup', self.run_backup))
        self.updater.dispatcher.add_handler(
            CommandHandler('show_backup_age',
                           self.show_backup_age))
        self.updater.dispatcher.add_handler(
            CommandHandler('hdd_smart_test', self.hdd_smart_test))
        self.updater.dispatcher.add_handler(
            CommandHandler('ifconfig_json_request',
                           self.ifconfig_json_request))
        self.updater.dispatcher.add_handler(
            CommandHandler('show_free_file_storage',
                           self.show_free_file_storage))

        # waiting for telegram commands
        self.updater.start_polling()
        self.updater.idle()

    def help(self, bot, update) -> None:
        """
        telegram command
        show all possible commands
        """
        update.message.reply_text(
            '/help /run_backup /hdd_smart_test')

    def run_backup(self, bot=None, update=None) -> None:
        # backup files
        backup_dirs = dict(self.conf.items('BackupDirs'))

        for key, value in backup_dirs.items():

            backup_path = path.join(self.conf['Server']['ArchivDir'], key)

            # check if backup_path exists & create it when necessary
            if not path.exists(backup_path):
                makedirs(backup_path)

            # check if backup_path is a directory
            if not path.isdir(backup_path) & path.exists(backup_path):
                waring_text = '%s no directory or not exists' % backup_path
                logging.warning(waring_text)
                send_mail.send_simple_message(
                    self.conf,
                    waring_text,
                    waring_text)
                self.updater.bot.send_message(chat_id=self.conf['TelegramBot']['chat'], text=waring_text)

            else:
                # move the backup files
                if self.conf['Server']['mode'] == "active":
                    archiv_files.archiv_files(
                        value,
                        backup_path,
                        self.conf['Server']['file_typ']
                    )

                # check if the backup directory is outdated
                if not check_backup.check_backup(backup_path, self.conf['Time']['days']):
                    msg = 'Backup "%s" is out of date, please check if the backup run correctly!' % key

                    send_mail.send_simple_message(
                        self.conf,
                        "Warning: Backup is out of Date!",
                        msg)

                    logging.warning("Mail was send reason: %s is out of date" % key)
                    self.updater.bot.send_message(chat_id=self.conf['TelegramBot']['chat'], text=msg)

    def show_backup_age(self, bot=None, update=None) -> None:
        backup_dirs = dict(self.conf.items('BackupDirs'))

        for key, value in backup_dirs.items():
            backup_path = path.join(self.conf['Server']['ArchivDir'], key)
            output = "{}: {}".format(key, get_directory_age(backup_path))
            self.updater.bot.send_message(chat_id=self.conf['TelegramBot']['chat'],
                                          text=output)

    def hdd_smart_test(self, bot, update) -> None:
        # HDD SMART test
        result = hdd_smart_test.main(self.conf)

        self.updater.bot.send_message(chat_id=self.conf['TelegramBot']['chat'], text=result)

    def ifconfig_json_request(self, bot, update) -> None:
        # return http://ifconfig.co/json request to string
        ifconfig_json_url = 'http://ifconfig.co/json'

        try:
            response = requests.get(ifconfig_json_url)
        except requests.exceptions.ConnectionError as e:
            self.updater.bot.send_message(chat_id=self.conf['TelegramBot']['chat'], text="Error: {}".format(e))
            return None

        if response.ok:
            json_data = json.loads(response.content)

            json_content = ""
            for key in json_data:
                json_content += "{}: {}\n".format(key, json_data[key])

            self.updater.bot.send_message(chat_id=self.conf['TelegramBot']['chat'], text=json_content)
        else:
            self.updater.bot.send_message(chat_id=self.conf['TelegramBot']['chat'], text=response.raise_for_status())

    def show_free_file_storage(self, bot, update) -> None:
        # run df -hl in shell and return the output to telegram
        response = subprocess.run("df -hl 1>&2",
                                  shell=True, stderr=subprocess.PIPE)
        self.updater.bot.send_message(chat_id=self.conf['TelegramBot']['chat'], text=response.stderr.decode("utf-8"))
