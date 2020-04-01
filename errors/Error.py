import discord
from discord.ext import tasks,commands
from discord.utils import get
import os

class Error(commands.Cog):
    def __init__(self,client):
        self.client = client

    #A Simple error handle if the user does not pass all the required arguments
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.author.send("Oops seems like your messing an argument for this command, please type $help for the list of commands!")
            await ctx.message.delete()
    #A simple error handle if a user tries to pass a command that does not exist it will give them an error message.
    @Commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.author.send(f"{ctx.author.metion}, the command you tried to enter does not exist! Please type $help for the list of commands!")
            await ctx.message.delete()

def setup(client):
    client.add_cog(Error(client))
