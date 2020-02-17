import discord
from discord.ext import commands
from discord.utils import get
import os
import random
import praw
class reddit(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def reddit(self,ctx,message: str = None):
        subreddit = reddit.subreddit('memes')
        top_subreddit = subreddit.top(limit=100)
        reddit = praw.Reddit(client_id='IifJXvTx06bvzQ', \
                     client_secret='H-649AGpK9NuCcJOkXlGWBdIkSQ', \
                     user_agent='LouieBot', \
                     username='LouieKB', \
                     password='yeetus450036235')
        if message == None:
            await ctx.message.delete()
            await ctx.author.send(top_subreddit)

def setup(client):
    client.add_cog(reddit(client))
