import discord
from discord.ext import commands
from discord.utils import get
import os

class random(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.lower('yeet'):
            await message.author.send("Always stay yeeting!")
            await message.delete()
