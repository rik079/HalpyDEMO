"""
HalpyDEMO v0.1

Copyright (c) 2021 The Hull Seals,
All rights reserved.

Licensed under the GNU General Public License
See license.md

"""

import discord

cmds = {}

def Command(name: str):
    def deco(function):
        if name in cmds.keys():
            raise KeyError("Command names must be unique")
        cmds[name] = function
        return function
    return deco

@Command("about")
async def cmd_about(bot, ctx: discord.Message):
    ctx.channel.send("This is a test of the about command")