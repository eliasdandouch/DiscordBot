import discord
from discord.ext import tasks,commands
from discord.utils import get
import os

class NoCommand(commands.Cog):
    def __init__(self,client):
        self.client = client

  #A simple error handle if a user tries to pass a command that does not exist it will give them an error message.
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.author.send(f"{ctx.author.mention}, the command you tried to enter does not exist! Please type $help for the list of commands!")
            await ctx.message.delete()



def setup(client):
    client.add_cog(NoCommand(client))
