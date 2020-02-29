import discord
from discord.ext import commands
from discord.utils import get
import os
import logging



class Report(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command(aliases=['report','reportuser'])
    async def report_user(self,ctx,member: discord.Member,option: int = None):
        if option == 1:
            await ctx.author.send(f"{ctx.message.author.mention}, Thank you {member.mention} has been reported for racism.")
            await ctx.message.delete()
            print(f"{ctx.message.author.mention}, has reported {member.mention} for {option}")
        if option == 2:
            await ctx.author.send(f"{ctx.message.author.mention}, Thank you {member.mention} has been reported for spam.")
            await ctx.message.delete()
            print(f"{ctx.message.author.mention}, has reported {member.mention} for {option}")
        if option == 3:
            await ctx.author.send(f"{ctx.message.author.mention}, Thank you {member.mention} has been reported for making threats to other users.")
            await ctx.message.delete()
            print(f"{ctx.message.author.mention}, has reported {member.mention} for {option}")

        ######If the user does not pass anything######
        if option == None and member == None:
            await ctx.author.send(f"{ctx.message.author.mention}, To report a user you must pass a reason, EX: $report @user#0001 (1,2,3,4)")
            await ctx.message.delete()
        if member == None:
            await ctx.author.send(f"{ctx.message.author.mention}, To report a user you must pass a user, EX: $report @user#0001 (1,2,3,4)")
            await ctx.message.delete()
        if option == None:
            await ctx.author.send(f"{ctx.message.author.mention}, To report a user you must pass a reason, EX: $report @user#0001 (1,2,3,4)")
            await ctx.message.delete()


def setup(client):
    client.add_cog(Report(client))
