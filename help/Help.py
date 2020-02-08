import discord
from discord.ext import commands
from discord.utils import get
import os
class help(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self,message):
        embed = discord.Embed(
        title = 'LouieBot'
        )
        embed.add_field(name='About', value="This Bot is very simple and is not intended to be complex or to have complex features. This bot was designed to pervent spam in the chat, So simply every command you type will be cleared and the result of the command will be DM'd to you. \nhttps://cdn.discordapp.com/attachments/672922054500024323/675232581322801172/tenor.gif", inline=True)
        if message.content.startswith('.about'):
            await message.delete()
            await message.author.send(embed=embed)





def setup(client):
    client.add_cog(help(client))
