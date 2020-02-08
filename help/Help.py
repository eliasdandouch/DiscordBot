import discord
from discord.ext import commands
from discord.utils import get
import os

class help(commands.Cog):
    def __init__(self,client):
        self.client = client
#Sends User Embeded Message w/ list of bot commands and what they do.
    @commands.Cog.listener()
    async def on_message(self,message):
        channels = ['general']
        embed = discord.Embed(
        title = 'Bot Commands',
        colour = discord.Colour.blue()
        )
        embed.set_author(name='LouieBot')
        embed.add_field(name='$flip', value='Flips a coin',inline=True)
        embed.add_field(name='$ping', value='Tells you the ping of the bot (Admin Only)', inline=True)
        embed.add_field(name='$clear', value='$clears previous command, this command can be given a value. (ex:$clear amount) (Admin Only)', inline=True)
        embed.add_field(name='.about', value='Tells you the purpose of the Bot!', inline=True)
        if message.content.startswith('.help'):
            await message.author.send(embed=embed)
            if str(message.channel) in channels:
                if message.content.startswith('.help'):
                    await message.delete()

def setup(client):
    client.add_cog(help(client))
