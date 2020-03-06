import discord
from discord.ext import commands
from discord.utils import get
import os


class MinecraftServer(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command(aliases=['minecraft','mcip'])
    async def mc(self,ctx,password: str = os.environ['PASSWORD'],server: str = None,*,vanillaserver: str = os.environ['VANILLASERVER'],ftbserver: str = os.environ['FTBSERVER']):
        if password == os.environ['PASSWORD'] and server == 'vanilla':
            await ctx.author.send(f"{ctx.message.author.mention}, Congratulations! You've entered the right password")
            await ctx.author.send(f"{ctx.message.author.mention}, the IP to the Vanilla Sever is {os.environ['VANILLASERVER']}")
            await ctx.message.delete()
        elif password == os.environ['PASSWORD'] and server == 'ftb':
            await ctx.author.send(f"{ctx.message.author.mention}, Congratulations! You've entered the right password")
            await ctx.author.send(f"{ctx.message.author.mention}, the IP to the Modded FTB Direwolf 1.12 Sever is {os.environ['VANILLASERVER']}")
            await ctx.message.delete()
        elif password == os.environ['PASSWORD'] and server == None:
            await ctx.author.send(f"{ctx.message.author.mention}, Congratulations! You've entered the right password BUT I can't give you an IP if I don't know which server please specificy! $mcip (ftb,vanilla)")
        elif password.upper is not os.environ['PASSWORD']:
            await ctx.author.send(f"{ctx.message.author.mention}, Incorrect! Either you've typed the password incorrectly or you were given a bad password. Please contact @Louie#0002.")
            await ctx.message.delete()
        else:
            return



def setup(client):
    client.add_cog(MinecraftServer(client))
