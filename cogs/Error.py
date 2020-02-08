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
            await ctx.author.send('Please pass in all required arguements for the command to work. Your message has been deleted.')
            await ctx.message.delete()





def setup(client):
    client.add_cog(Error(client))
