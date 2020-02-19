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

    @commands.command(aliases=['c','C'])
    async def convert(self,ctx,conversion1: str.upper = None,conversion2: str.upper = None, number: int = None):
        mp = ("Missing parameterer, please type $help for the list of commands.")
        if conversion1 and conversion2 and number == None: #if the user doesnt type two converters and a number it will delete the message.
            await ctx.message.delete()
            await ctx.author.send(mp)
        if conversion1 == None: #if the user does not type one of the converters it will delete the message.
            await ctx.message.delete()
            await ctx.author.send(mp)
        if conversion2 == None: #if the user does not type one of the converters it will delete the message.
            await ctx.message.delete()
            await ctx.author.send(mp)
        if number == None: #if the user does not type the # it will delete the message.
            await ctx.message.delete()
            await ctx.author.send(mp)
        if conversion1 == None and number == None: #if the user does not type one converter and doesn't type a # it will delete the message.
            await ctx.message.delete()
            await ctx.author.send(mp)
        if conversion2 == None and number == None: #if the user does not type one converter and doesn't type a # it will delete the message.
            await ctx.message.delete()
            await ctx.author.send(mp)
        if number >= 101:
            await ctx.message.delete()
            await ctx.author.send(mp)

        if conversion1 == 'C' and conversion2 == 'F' and number <= 100:
            a = 9
            b = 5
            c = 32
            await ctx.author.send(a/b*number+c)
            await ctx.message.delete()
        if conversion1 == "F" and conversion2 == 'C' and number <= 100: #Does F C Conversion
            await ctx.author.send(a/b*number-c)
            await ctx.message.delete()
        if conversion1 == 'C' and conversion2 == 'K' and number <= 100: #Does C K Conversion
            await ctx.author.send(number+273.15)
            await ctx.message.delete()
        if conversion1 == 'F' and conversion2 == 'C' and number <= 100:
            await ctx.author.send("a/b*number-c")
            await ctx.message.delete()
    @commands.command()
    async def time(self,ctx, arg: int = None):
        format = "%H:%M:%S"
        if arg == None:
            now = datetime.datetime.now().strftime("%H:%M")
            await ctx.author.send(now)
            await print(now)
            await ctx.message.delete()
        else:
            await ctx.author.send("Oops seems like you've entered an invalid command, please use $help for the list of the bot's commands.")
            await ctx.message.delete()


def setup(client):
    client.add_cog(FunCommands(client))
