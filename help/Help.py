import discord
from discord.ext import commands
from discord.utils import get
import os
import random

class help(commands.Cog):
    def __init__(self,client):
        self.client = client


#Sends User Embeded Message w/ list of bot commands and what they do.
    @commands.command(aliases=['Help','commands','Commands'])
    async def help(self,ctx,arg: int = None):
        channels = ['general']
        embed = discord.Embed(
        title = 'Bot Commands',
        colour = discord.Colour.green()
        )
        embed.set_author(name='LouieBot')
        embed.add_field(name='$flip', value='Flips a coin',inline=True)
        embed.add_field(name='$ping', value='Tells you the ping of the bot (Admin Only)', inline=True)
        embed.add_field(name='$clear', value='$clears previous command, this command can be given a value. (ex:$clear amount) (Admin Only)', inline=True)
        embed.add_field(name='$about', value='Tells you the purpose of the Bot!', inline=True)
        embed.add_field(name='$convert', value="Converts ('Celisus,Fahrenheit,Kelvin') ($convert {C,F,K} {C,F,K} value)", inline=True)
        embed.add_field(name='$8ball',value="It's a magic eight ball. This command must be given a message ($magicball message)")
        if arg == None:
            await ctx.author.send(embed=embed)
            await ctx.message.delete()
        else:
            await ctx.author.send("Oops seems like you've entered an invalid command, please use $help for the list of the bot's commands.")
            await ctx.message.delete()


def setup(client):
    client.add_cog(help(client))
