import os
import logging
import weakref
import telethon.sync as telethon

from .credentials import API_ID, API_HASH, CLIENT_PHONE, BOT_TOKEN, CHANNEL_ID, CHANNEL_ACCESS_HASH


class AppInteraction():
    _CLIENT_SESSION = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'client.session')
    _BOT_SESSION = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'members_tracker_bot.session')

    def __init__(self):
        self._client = telethon.TelegramClient(self._CLIENT_SESSION, API_ID, API_HASH)
        self._client.start(phone=CLIENT_PHONE)
        self._my_id = self._client.get_me().id

        self._bot = telethon.TelegramClient(self._BOT_SESSION, API_ID, API_HASH)
        self._bot.start(bot_token=BOT_TOKEN)

        self._input_channel = telethon.types.InputChannel(CHANNEL_ID, CHANNEL_ACCESS_HASH)

    def get_members(self):
        return self._client.get_participants(self._input_channel)

    def notify(self, message):
        self._bot.send_message(self._my_id, message, silent=False)

    def get_notification_handler(self):
        return NotificationHandler(self)


class NotificationHandler(logging.StreamHandler):
    def __init__(self, app):
        super(NotificationHandler, self).__init__(self)
        self.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))

        self._app = weakref.ref(app)

    def emit(self, record):
        msg = self.format(record)
        self._app().notify(msg)

