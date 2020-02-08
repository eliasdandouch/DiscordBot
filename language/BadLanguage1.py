import discord
from discord.ext import commands
from discord.utils import get
import os

client = commands.Bot(command_prefix = ',')
badwords = {'nigger,test,summit'}

class BadLanguage1(commands.Cog):
    def __init__(self,client):
        self.client = client

    #Racist Ban and Clear Terms
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.content.startswith('nigger'):
            await message.delete()
            await message.author.send("Your message has been deleted due to your bad language.")


def setup(client):
    client.add_cog(BadLanguage1(client))
