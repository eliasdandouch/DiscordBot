import discord
from discord.ext import commands
from discord.utils import get
import os
import random

class FunCommands(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def flip(self,ctx,message : str = None):
        cointoss = 'The result of the cointoss is: Heads','The result of the cointoss is: Tails'
        DM = ['dm','DM']
        if message == None:                     #If the user just types $flip it will enter the result of the cointoss in general.
            await ctx.send(random.choice(cointoss))
            await ctx.message.delete()
        if message == 'DM' and 'dm':            #If the user enters $flip dm or $flip DM it will DM the result of the cointoss.
            await ctx.author.send(random.choice(cointoss))
            await ctx.message.delete()
        #if message is not != 'DM' or None:
            #await ctx.author.send("the $flip command you've entered is invalid, please use '$help' for the list of the commands.")

def setup(client):
    client.add_cog(FunCommands(client))
