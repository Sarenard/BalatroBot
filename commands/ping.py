from discord.ext import commands
import asyncio
import discord
import random
import sys
import os

class Ping(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong")

async def setup(client):
    await client.add_cog(Ping(client))