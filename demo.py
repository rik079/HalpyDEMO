"""
HalpyDEMO v0.1

Copyright (c) 2021 The Hull Seals,
All rights reserved.

Licensed under the GNU General Public License
See license.md

"""

import discord
import configparser

from src.facts import Facthandler

config = configparser.ConfigParser()
config.read("config/config.ini")

class DemoBot(discord.Client):

    def __init__(self):
        # Load facts first
        self.facthandler = Facthandler(config['Database']['path'])
        super().__init__()


HalpyDemo = DemoBot()

@HalpyDemo.event
async def on_ready():
    print(f"Bot logged in as '{HalpyDemo.user}'")

HalpyDemo.run(config['Discord']['token'])
