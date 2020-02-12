import discord
from discord.ext import commands
from discord.utils import get
import os
import random

class FunCommands(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def flip(self,ctx,member : discord.Member):
        cointoss = 'Heads','Tails'
        if member == None:
            await ctx.author.send()

def setup(client):
    client.add_cog(FunCommands(client))
