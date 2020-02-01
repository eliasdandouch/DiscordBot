import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
import random

client = commands.Bot(command_prefix = '.')

client.load_extension('cogs.MiscCommands')
client.load_extension('cogs.CommandEvents')

#Calling Discord Account
client.run("NjcyODc2MjQ3ODA5OTE2OTQ5.XjR26Q.JpaNNxI6xVIQ0Cd0bAtnOt7rX3w")
