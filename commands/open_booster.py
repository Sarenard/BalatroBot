from discord.ext import commands
from datetime import datetime
import asyncio
import discord
import random
import json
import sys
import os
import database.jokers as JokersDB
from utility.add_user import *

class Open(commands.Cog): 
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def booster(self, ctx):
        with open("database/db.json", "r+") as file:
            db = json.load(file)
            author_id = str(ctx.author.id)
            
            if author_id not in db:
                add_user(author_id)
                db = json.load(file)
            
            if db[author_id]["last_open"] != datetime.today().strftime("%d-%m-%Y"):
                db[author_id]["boosters_opened"] = 0
                db[author_id]["last_open"] = datetime.today().strftime("%d-%m-%Y")
            
            if db[author_id]["boosters_opened"] >= 3:
                await ctx.send("You already opened 3 booster packs today, come back tomorrow !")
                return

            for _ in range(4):
                rand = random.uniform(0, 1)

                if rand < 0.7:
                    commons = list(filter(lambda j: j.rarity == "Common", JokersDB.jokers))
                    joker = random.choice(commons)
                elif rand < 0.95:
                    uncommons = list(filter(lambda j: j.rarity == "Uncommon", JokersDB.jokers))
                    joker = random.choice(uncommons)
                elif rand < 0.993:
                    rares = list(filter(lambda j: j.rarity == "Rare", JokersDB.jokers))
                    joker = random.choice(rares)
                else:
                    legendaries = list(filter(lambda j: j.rarity == "Legendary", JokersDB.jokers))
                    joker = random.choice(legendaries)

                await ctx.send(f"You just got **{joker.joker_name}** !")
                db[author_id]["jokers"].append(joker.joker_name)
            
            db[author_id]["boosters_opened"] += 1

            file.seek(0)
            json.dump(db, file)


async def setup(client):
    await client.add_cog(Open(client))