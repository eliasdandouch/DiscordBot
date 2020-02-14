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
        cointoss = 'The result of the cointoss is: Heads','The result of the cointoss is: Tails'
        DM = ['dm','DM']
        if message == None:                     #If the user just types $flip it will enter the result of the cointoss in general.
            await ctx.send(random.choice(cointoss))
            await ctx.message.delete()
        if message == 'DM' or 'dm':            #If the user enters $flip dm or $flip DM it will DM the result of the cointoss.
            await ctx.author.send(random.choice(cointoss))
            await ctx.message.delete()

    @commands.command()
    async def magicball(self,ctx,message : str = None):
        if message == None:
            await ctx.author.send("For the 8Ball command to work you must enter a message after the command.")
            await ctx.message.delete()
        else:
            await ctx.author.send(random.choice(['It is certain.','It is decidedly so.',' Without a doubt.','Yes - definitely.','You may rely on it.','As I see it, yes.','Most likely.',' Outlook good.','Yes.','Signs point to yes.','Reply hazy, try again.','Ask again later.','Better not tell you now.',' Cannot predict now.','Concentrate and ask again.',"Don't count on it.","My reply is no."," My sources say no.","Outlook not so good.",'Very doubtful.']))
            await ctx.message.delete()
    @commands.command()
    async def time(self,ctx,message : str = None):
        pacific = now_utc.astimezone(timezone('US/Pacific'))
        await ctx.say(pacific.strftime(fmt) + ("US/Pacific"))


def setup(client):
    client.add_cog(FunCommands(client))
