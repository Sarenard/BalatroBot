from discord.ext.commands import has_permissions, CheckFailure
from discord.ext import commands,tasks
import asyncio
import discord
import json
import time 
import os

import os, sys
parentdir = os.path.dirname(__file__)
sys.path.insert(0, parentdir)

config_private = json.load(open("config/config_private.json"))
config = json.load(open("config/config.json"))

intents = discord.Intents().all()
client = commands.Bot(command_prefix=config["discord"]["prefixs"], intents=intents)
client.remove_command('help')

async def init_cogs():
    for fichier in os.listdir("./commands"):
        if fichier.endswith(".py"):
            try:
                await client.load_extension(f"commands.{fichier[:-3]}")
            except Exception as e:
                print(e)

asyncio.run(init_cogs())

client.run(config_private["discord"]["token"])