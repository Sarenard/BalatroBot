from discord.ext import commands
import asyncio
import discord
import random
import sys
import os

import enum

import database.jokers as JokersDB

class Info(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def info(self, ctx, *name):
        # the joker we are looking for
        try:
            joker = list(filter(lambda j: j.joker_name == " ".join(name), JokersDB.jokers))[0]
            await ctx.send(f"\
# {joker.joker_name}\n\n\
**Rarity** : {joker.rarity}\n\
**Info** : {joker.info}\n\
**Rarity** : {joker.rarity}\n\
**Price** : {joker.price}\
")
        except IndexError:
            await ctx.send("This joker does not exist.")

async def setup(client):
    await client.add_cog(Info(client))