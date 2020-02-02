import discord
from discord.ext import commands
from discord.utils import get
import os

class AdminCommands(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=None)

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=None)

def setup(client):
    client.add_cog(AdminCommands(client))
