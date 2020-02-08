import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
import random

class MiscCommands(commands.Cog):
    def __init__(self,client):
        self.client = client

    #MiscCommands
    @commands.command()
    @commands.has_any_role('Elias','Gavin', 123206185326215169)
    async def ping(self,ctx):
        await ctx.send("Pong!")

    @commands.command()
    @commands.has_any_role('Elias','Gavin', 123206185326215169)
    async def clear(self,ctx,amount=3):
        await ctx.channel.purge(limit=amount)

    @commands.command()
    async def flip(self,ctx):
        cointoss = ['The result of the coin toss is: Heads','The result of the coin toss is: Tails']
        await ctx.send(random.choice(cointoss))




def setup(client):
    client.add_cog(MiscCommands(client))
