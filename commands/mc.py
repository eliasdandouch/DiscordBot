import discord
from discord.ext import commands
from discord.utils import get
import os


class MC(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command(aliases=['mc','minecraft','minecraftserver'])
    async def mc(self,password: str = None,*,mcserver: str = '1.1.1.1'):
        if password.upper == 'jamalhub.com':
            await ctx.author.send(f"{ctx.message.author.mention}, Congratulations! You've entered the right password")
            await ctx.author.send(f"{ctx.message.authir.mention}, the IP to the sever is {mcserver}")
            await ctx.message.delete()
        else:
            await ctx.author.send(f"{ctx.message.author.mention}, Incorrect! Either you've typed the password incorrectly or you were given a bad password. Please contact @Louie#0002.")
            await ctx.message.delete()



def setup(client):
    client.add_cog(MC(client))
