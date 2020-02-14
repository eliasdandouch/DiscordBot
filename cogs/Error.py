import discord
from discord.ext import commands
from discord.utils import get
import os

class Error(commands.Cog):
    def __init__(self,client):
        self.client = client

    #A Simple error handle if the user does not pass all the required arguments
    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.author.send("Oops seems like you've eneted an invalid command using the please type '$help' for the list of commands.")
            await print(print('Error in {0.command.qualified_name}: {1}'.format(ctx, error)))
            await ctx.message.delete()

def setup(client):
    client.add_cog(Error(client))
