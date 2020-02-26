import discord
from discord.ext import commands


class Convert(commands.Cog):
    def __init__(self,client):
        self.client = client

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
##############################################################################
        if conversion1 == 'C' and conversion2 == 'F' and number <= 100:
            a = 9
            b = 5
            c = 32
            CF = a/b*number+c
            CK = number+273.15
            await ctx.author.send(CF)
            await ctx.message.delete()
        elif conversion1 == "F" and conversion2 == 'C' and number <= 100: #Does F C Conversion
            await ctx.author.send(a/b*number-c)
            await ctx.message.delete()
        elif conversion1 == 'C' and conversion2 == 'K' and number <= 100: #Does C K Conversion
            await ctx.author.send(CK)
            await ctx.message.delete()
        else:
            await ctx.author.send(mp)



def setup(client):
    client.add_cog(Convert(client))
