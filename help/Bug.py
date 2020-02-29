import discord
from discord.ext import commands
import os

class Bug(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command(aliases=['bug','BUG'])
    async def Bug(self,ctx,arg: int = None):
        if arg == None:
            await ctx.author.send(f"{ctx.message.author.mention}, If you would like to report a bug related to the bot please report it here: https://github.com/eliasdandouch/LouieBot_Discord/issues")
            await ctx.message.delete()
        elif arg != 100:
            await ctx.author.send(f"{ctx.message.author.mention}, It seems like you've typed an incorrect command, please use $help for the list of commands.")
            await ctx.message.delete()
        else:
            return



def setup(client):
    client.add_cog(Bug(client))
