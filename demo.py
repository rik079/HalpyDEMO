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
from src.commands import cmds

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

@HalpyDemo.event
async def on_message(message: discord.Message):
    if message.author == HalpyDemo.user or not message.content.startswith(config['Discord']['prefix']):
        return  # Ignore our own messages
    opdr = message.content[1:].split()[0]
    fact = HalpyDemo.facthandler.get_fact(opdr, message.content.split()[1:])  # Fact, args
    # Now we check if the message is a command or a fact
    if opdr in cmds.keys():
        return await cmds[opdr](HalpyDemo, message, message.content.split()[1:])  # Bot, context, arguments
    elif fact:
        return await message.channel.send(fact)

HalpyDemo.run(config['Discord']['token'])
