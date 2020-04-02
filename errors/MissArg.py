import discord
from discord.ext import tasks,commands
from discord.utils import get
import os

class MissArg(commands.Cog):
    def __init__(self,client):
        self.client = client

    #A Simple error handle if the user does not pass all the required arguments
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.author.send(f"{ctx.author.mention}, Oops seems like your messing an argument for this command, please type $help for the list of commands!")
            await ctx.message.delete()


def setup(client):
    client.add_cog(MissArg(client))
