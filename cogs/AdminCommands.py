import discord
from discord.ext import commands
from discord.utils import get
import os

class AdminCommands(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    @commands.has_any_role('Elias','Gavin', 123206185326215169)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=None)
        await ctx.author.send(f'{member.mention}, has been successfully kicked from the server.')

    @commands.command()
    @commands.has_any_role('Elias','Gavin', 123206185326215169)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
            await member.ban(reason=None)
            await ctx.author.send(f'{member.mention}, has been successfully banned from the server.')

def setup(client):
    client.add_cog(AdminCommands(client))
