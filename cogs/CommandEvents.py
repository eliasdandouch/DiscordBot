import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
import random

class CommandEvents(commands.Cog):
    def __init__(self,client):
        self.client = client

    #CommandEvents
    @commands.Cog.listener()
    async def on_ready(self):
        print("The bot is online and has connected to the server successfully.")

    @commands.Cog.listener()
    async def clear(self,message):
        if message.author == client.user:
            return
        if message.content.startswith('hello'):
            await message.channel.send("Hello!")
            await client.process_commands(message)


def setup(client):
    client.add_cog(CommandEvents(client))
