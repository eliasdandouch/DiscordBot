import discord
from discord.ext import commands
from discord.utils import get
import os
import random
from datetime import datetime
from pytz import timezone



class FunCommands(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def flip(self,ctx,message : str = None):
        cointoss = 'Heads','Tails'
        channel = ['general']
        DM = ['dm','DM']
        if message == None:                     #If the user just types $flip it will enter the result of the cointoss in general.
            await channel.send(f"The result of the cointoss is: {random.choice(cointoss)}")
            await ctx.message.delete()
        if message == 'DM' or 'dm':            #If the user enters $flip dm or $flip DM it will DM the result of the cointoss.
            await ctx.author.send(f"{ctx.message.author.mention}, The result of the cointoss is: {random.choice(cointoss)}")
            await ctx.message.delete()

    @commands.command(aliases=['8ball'])
    async def _8ball(self,ctx,message : str = None):
        if message == None:
            await ctx.author.send("For the 8Ball command to work you must enter a message after the command.")
            await ctx.message.delete()
        else:
            await ctx.author.send(random.choice(['It is certain.','It is decidedly so.',' Without a doubt.','Yes - definitely.','You may rely on it.','As I see it, yes.','Most likely.',' Outlook good.','Yes.','Signs point to yes.','Reply hazy, try again.','Ask again later.','Better not tell you now.',' Cannot predict now.','Concentrate and ask again.',"Don't count on it.","My reply is no."," My sources say no.","Outlook not so good.",'Very doubtful.']))
            await ctx.message.delete()

def setup(client):
    client.add_cog(FunCommands(client))
