import discord
from discord.ext import commands
from discord.utils import get
from datetime import datetime
import pytz
tz_CA = pytz.timezone('America/Los_Angeles')
CA = datetime.now(tz_CA)
time = ("The current time in Ventura, California is:", CA.strftime("%H:%M:%S"))
