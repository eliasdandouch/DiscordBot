import discord
from discord.ext import tasks,commands
from discord.utils import get
import os

class AdminCommands(commands.Cog):
    def __init__(self,client):
        self.client = client
    channels = ['general']

    @commands.command()
    @commands.has_any_role('Elias','Gavin', 123206185326215169)
    async def kick(self, ctx, member : discord.Member, reason=None):
        await member.kick(reason=reason)
        await ctx.message.delete()
        await ctx.author.send(f'{member.mention}, has been successfully kicked from the server for {reason}.')
        print(f"{ctx.message.author.mention}, has kicked {member.mention} for {reason}")
    @commands.command()
    @commands.has_any_role('Elias','Gavin', 123206185326215169)
    async def ban(self, ctx, member : discord.Member, reason=None):
            await member.ban(reason=None)
            await ctx.message.delete()
            await ctx.author.send(f'{member.mention}, has been successfully banned from the server for {reason}.')
            print(f"{ctx.message.author.mention}, has banned {member.mention} for {reason}")
    @commands.command()
    @commands.has_any_role('Elias','Gavin', 123206185326215169)
    async def clear(self,ctx,arg: int = None):
        if arg == None:
            await ctx.message.delete()
        if arg <= 100:
            await ctx.channel.purge(limit = arg)
            print(f"{ctx.message.author.mention}, has cleared {arg} messages")
        if arg > 100:
            await ctx.author.send(f"{ctx.message.author.mention}, Unfortunately the bot can only clear 100 messages at a time otherwise the server and the bot will lag!")
            await ctx.message.delete()
            print(f"{ctx.message.author.mention}, has ran the $clear command but typed a # over 100")
        else:
            return

    @commands.command()
    @commands.has_any_role('Elias','Gavin', 123206185326215169)
    async def mute(self,ctx,member: discord.Member):
        if member == None:
            await ctx.author.send(f"{ctx.author.mention}, please pass a user to mute!")
            await ctx.message.delete()
        else:
            await member.mute()
            await ctx.author.send(f"{ctx.author.mention}, {member.mention} has been muted!")
            await ctx.message.delete()


def setup(client):
    client.add_cog(AdminCommands(client))
