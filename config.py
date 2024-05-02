

import logging

from telethon import TelegramClient

from os import getenv
from SHUKLASPAM.data import SHASHANK


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR SHUKLA'SBOTS
API_ID = 25992525
API_HASH = "190ab5aaeb8886ab7c986eb54959377c"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

BOT_TOKEN = getenv("BOT_TOKEN", default=None)


SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="5730490876").split()))
for x in SHASHANK:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="5730490876"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
