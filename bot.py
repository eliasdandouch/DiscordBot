import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
import random
import re

client = commands.Bot(command_prefix = ',')

client.load_extension('cogs.MiscCommands')
client.load_extension('cogs.AdminCommands')
client.load_extension('cogs.BotOnline')
client.load_extension('language.BadLanguage1')
client.load_extension('language.BadLanguage2')

#Calling Discord Account
client.run("TOKEN")
