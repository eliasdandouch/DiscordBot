import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
import random
import re

client = commands.Bot(command_prefix = ',')

class BadLanguage2(commands.Cog):
    def __init__(self,client):
        self.client = client

    #Racist Ban and Clear Terms
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.content.startswith("NIGGER"):
            await message.delete()
            await message.author.send("Your message has been deleted due to your bad language.")


def setup(client):
    client.add_cog(BadLanguage2(client))
