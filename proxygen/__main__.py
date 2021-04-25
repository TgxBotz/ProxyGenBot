"""
ProxyGenBot
Copyright (C) 2021 TgxBotz

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See < https://github.com/TgxBotz/ProxyGenBot/blob/master/LICENSE > 
for the license.
"""


import glob
from pathlib import Path
from proxygen.utils import load_plugins
import logging
from proxygen import ProxyGen, LOGGER
from Configs import Config

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "proxygen/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))


print("Successfully Started ProxyGenBot!")
print("Visit @TgxBots")

if __name__ == "__main__":
    ProxyGen.run_until_disconnected()
