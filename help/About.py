import discord
from discord.ext import commands
from discord.utils import get
import os
class About(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command(aliases=['About'])
    async def about(self,ctx,arg: int = None):
        embed = discord.Embed(
        title = 'LouieBot'
        )
        embed.add_field(name='About', value="This Bot is very simple and is not intended to be complex or to have complex features. This bot was designed to pervent spam in the chat, So simply every command you type will be cleared and the result of the command will be DM'd to you. \nhttps://cdn.discordapp.com/attachments/672922054500024323/675232581322801172/tenor.gif", inline=True)
        if arg == None:
            await ctx.author.send(embed=embed)
            await ctx.message.delete()
        else:
            ctx.send.author("Oops seems like you've entered an invalid command, please use $help for the list of the bot's commands.")
            await ctx.message.delete()

    async def dev(self,ctx,*,arg: int = None):
        if arg == None:
            await ctx.author.send(f'{mention.user}, This Bot was developed by Louie#0002!')
            await ctx.message.delete()
        else:
            await ctx.author.send("Oops seems like you've entered an invalid command, please use $help for the list of the bot's commands.")
            await ctx.message.delete()


def setup(client):
    client.add_cog(About(client))
