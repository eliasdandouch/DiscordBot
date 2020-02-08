import discord
from discord.ext import commands
from discord.utils import get
import os


client = commands.Bot(command_prefix = '$')
#Loads Basic Command Cogs
client.load_extension('cogs.MiscCommands')
client.load_extension('cogs.AdminCommands')
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
    game = discord.Game('Type ".help" in general for Bot commands')
    await client.change_presence(status=discord.Status.online, activity=game)
    print("The bot is online and has connected to the server successfully.")



#Calling Discord Account
client.run("NjcyODc2MjQ3ODA5OTE2OTQ5.XjYzig.mr3pMaHZgx4MmE1RLMCbAq75WgY")
