import discord
from discord.ext import commands
from discord.utils import get
import os

class BotOnline(commands.Cog):
    def __init__(self,client):
        self.client = client

        #CommandEvents
    @commands.Cog.listener()
    async def on_ready(self):
        print("The bot is online and has connected to the server successfully.")





def setup(client):
    client.add_cog(BotOnline(client))
