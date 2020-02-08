import discord
from discord.ext import commands
from discord.utils import get
import os
class about(commands.Cog):
    def __init__(self,client):
        self.client = client

#Sends User Embeded Message w/ list of bot commands and what they do.
    @commands.Cog.listener()
    async def on_message(self,message):
        embed = discord.Embed(
        title = 'Bot Commands',
        colour = discord.Colour.blue()
        )
        embed.set_author(name='LouieBot')
        embed.add_field(name='$flip', value='Flips a coin',inline=True)
        embed.add_field(name='.about', value='Tells you the purpose of the Bot!', inline=True)
        if message.content.startswith('.help'):
            await message.delete()
            await message.author.send(embed=embed)

def setup(client):
    client.add_cog(about(client))
