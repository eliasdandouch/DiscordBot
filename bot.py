import discord
from discord.ext import commands
from discord.utils import get
import os

bot_id = '672876247809916949'
client = commands.Bot(command_prefix = '$')
#Loads Basic Command Cogs
client.load_extension('cogs.MiscCommands')
client.load_extension('cogs.AdminCommands')
#Loads Error Handle Cog
client.load_extension('cogs.Error')
#Loads Bad Word Filter Cog5
client.load_extension('language.BadLanguage1')
client.load_extension('language.BadLanguage2')
client.load_extension('language.BadLanguage3')
client.load_extension('language.BadLanguage4')
client.load_extension('language.BadLanguage5')
client.load_extension('language.BadLanguage6')
client.load_extension('language.BadLanguage7')
client.load_extension('language.BadLanguage8')
client.load_extension('language.BadLanguage9')
#Loads Help Commands Cogs
client.load_extension('help.About')
client.load_extension('help.Help')

##Bot Status
@client.event
async def on_ready():
    print('-------------------------------------------------------------')
    print('Bot Name: ' + client.user.name)
    print('Bot ID: ' + bot_id)
    print('Discord Version: ' + discord.__version__)
    print("The bot is online and has connected to the server successfully.")
    game = discord.Game('Yeet | .help for Help!')
    print('-------------------------------------------------------------')
    await client.change_presence(status=discord.Status.online, activity=game)



#Calling Discord Account
client.run("NjcyODc2MjQ3ODA5OTE2OTQ5.Xj72vQ.8Hg55YpeXu3Tsma3dM1k2xENXS0")
