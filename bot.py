import discord
from discord.ext import commands
from discord.utils import get
import os

bot_id = '672876247809916949'
client = commands.Bot(command_prefix = '$')
client.remove_command('help')
#Loads Basic Command Cogs
client.load_extension('commands.AdminCommands')
client.load_extension('commands.FunCommands')
client.load_extension('commands.reddit')
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
    game = discord.Game('Yeet | $commands')
    print('-------------------------------------------------------------')
    await client.change_presence(status=discord.Status.online, activity=game)



#Calling Discord Account
client.run(os.environ['TOKEN'])
