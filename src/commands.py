"""
HalpyDEMO v0.1

Copyright (c) 2021 The Hull Seals,
All rights reserved.

Licensed under the GNU General Public License
See license.md

"""

import discord
import configparser
from typing import List
import re

config = configparser.ConfigParser()
config.read("config/config.ini")

cmds = {}

def Command(name: str):
    def deco(function):
        if name in cmds.keys():
            raise KeyError("Command names must be unique")
        cmds[name] = function
        return function
    return deco

@Command("about")
async def cmd_about(bot: discord.Client, ctx: discord.Message, args: List[str]):
    embed = discord.Embed(title="HalpyDEMO", colour=discord.Colour.orange(),
                          description="Hull Seals Demonstration Bot")
    embed.add_field(name="Developed by:", value="Rik079")
    embed.add_field(name="Active project:", value=config['Discord']['project'], inline=False)
    embed.set_footer(text="2021 The Hull Seals - All rights reserved",
                     icon_url="https://hullseals.space/images/emblem.png")
    await ctx.channel.send(embed=embed)

@Command("help")
async def cmd_help(bot: discord.Client, ctx: discord.Message, args: List[str]):
    embed = discord.Embed(title="Help", colour=discord.Colour.orange(),
                          description="For a list of common facts, please see "
                                      "https://hullseals.space/knowledge/books/irc/page/"
                                      "halpybot-command-and-fact-listing")
    embed.add_field(name=f"{config['Discord']['prefix']}help",
                    value="Show this message", inline=False)
    embed.add_field(name=f"{config['Discord']['prefix']}about",
                    value="Display information about the bot", inline=False)
    embed.add_field(name=f"{config['Discord']['prefix']}announce [PC/PS/XB] "
                         f"\"[CMDR]\" \"[System]\" [Hull %]",
                    value="Send a new case announcement to the appropriate channel.")
    await ctx.channel.send(embed=embed)

@Command("announce")
async def cmd_case(bot: discord.Client, ctx: discord.Message, args: List[str]):
    try:
        regex = re.compile(r"['\"](?P<CMDR>[\w ]*)['\"] ['\"](?P<System>[\w ]*)['\"] (?P<HullP>\d{2,3})") \
            .search(' '.join(args))
        platform = args[0].lower()
        hull = regex.group("HullP")
        cmdr = regex.group("CMDR")
        system = regex.group("System")
    except (AttributeError, IndexError):
        return await ctx.channel.send("Oops, looks like a formatting error. Please see !help for "
                                      "the correct announcement format")
    if not args[0].lower() in ("pc", "xb", "ps"):
        return await ctx.channel.send("Please specify a valid platform: PC, XB or PS.")
    message = f"xxxx {platform.upper()}CASE -- NEWCASE xxxx\n" \
              f"CMDR: {cmdr} -- Platform: {platform.upper()}\n" \
              f"System: {system} -- Hull: {hull}\n" \
              f"xxxxxxxx"
    channel = bot.get_channel(id=int(config['Announcer'][f"{platform.lower()}_channel"]))
    await channel.send(message)
