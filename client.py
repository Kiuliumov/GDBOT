# client module
import discord
import gd
from discord.ext import commands
from constants import PREFIX


intents = discord.Intents.default()
intents.message_content = True

gd_client = gd.Client()
client = commands.Bot(command_prefix=PREFIX, intents=intents)
