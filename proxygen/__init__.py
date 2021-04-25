"""
ProxyGenBot
Copyright (C) 2021 TgxBotz

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See < https://github.com/TgxBotz/ProxyGenBot/blob/master/LICENSE > 
for the license.
"""


import os
import logging
from telethon import TelegramClient
from Configs import Config

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

LOGGER = logging.getLogger(__name__)

API_ID = Config.API_ID
API_HASH = Config.API_HASH
TOKEN = Config.TOKEN

if API_ID is None or API_HASH is None:
       LOGGER.info("You forgot to add API_ID or API_HASH in vars!, Bot is quitting.")
       exit(0)

if TOKEN is None:
       LOGGER.info("You forgot to add bot token in vars!, Bot is quitting")
       exit(0)

bot = TelegramClient('ProxyGen', api_id=Config.API_ID, api_hash=Config.API_HASH)
ProxyGen = bot.start(bot_token=Config.TOKEN)

