import discord
from discord.ext import commands
from client import gd_client
from cls.Builders import Builder
import constants
from cls.Search import Search
from images import text_art
from cls.Loader import Loader
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='$', intents=intents)

builder = Builder()
search = Search()
loader = Loader()

@client.event
async def on_ready():
    print(client.user)
    print(client.user.id)
    try:
        synced = await client.tree.sync()
        print(f'Synced {len(synced)} command(s)')
        print(text_art.computer)
    except Exception as e:
        print(e)

@client.tree.command(name='ping', description='This is a ping command!')
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message('Pong!')

@client.tree.command(name='daily', description='Get the daily level in Geometry Dash')
async def daily(interaction: discord.Interaction):
    try:
        daily = await gd_client.get_daily()
        embed = await builder.make_level_embed(daily.id)
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        await interaction.response.send_message(f'An error has occurred!\n{str(e).capitalize()}')

@client.tree.command(name='weekly', description='Get the weekly level in Geometry Dash')
async def weekly(interaction: discord.Interaction):
    try:
        weekly = await gd_client.get_weekly()
        embed = await builder.make_level_embed(weekly.id)
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        await interaction.response.send_message(f'An error has occurred!\n{str(e).capitalize()}')

@client.tree.command(name='song', description='Get information about a song in Geometry Dash')
async def song(interaction: discord.Interaction, song_id: int):
    try:
        embed = await builder.make_song_embed(song_id)
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        await interaction.response.send_message(f'An error has occurred!\n{str(e).capitalize()}')

@client.tree.command(name='search', description='Search for a level in Geometry Dash')
async def search_level(interaction: discord.Interaction, name: str, depth: int = None):
    try:
        if depth:
            level_ids = await Search.search_level(name, depth)
        else:
            level_ids = await Search.search_level(name)
        await interaction.response.send_message(f'Searching for levels with name: {name}')
        for ID in level_ids:
            try:
                embed = await builder.make_level_embed(ID)
                await interaction.channel.send(embed=embed)
            except Exception as e:
                await interaction.channel.send(str(e))
    except Exception as e:
        await interaction.channel.send(f'An error has occurred!\n{str(e).capitalize()}')

@client.tree.command(name='find_user', description='Find a user in Geometry Dash')
async def find_user(interaction: discord.Interaction, username: str):
    try:
        embed = await builder.make_user_embed(username)
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        await interaction.response.send_message(f'An error has occurred!\n{str(e).capitalize()}')
@client.tree.command(name='load_user_levels',description='Loads user comments to a certain depth.')
async def load_user_levels(interaction: discord.Interaction,username: str,depth: int = 5):
    try:
        levels = await loader.load_levels(username)
        await interaction.response.send_message(f"{username}'s levels:")
        for index,level in enumerate(levels):
            index += 1
            if index > depth or index > 50:
                break
            try:
                embed = await builder.make_level_embed(level.id)
                await interaction.channel.send('https://i.imgur.com/IIpYiGq.png')
                await interaction.channel.send(embed=embed)
            except Exception as e:
                await interaction.channel.send(f'gd.py is still outdated for levels from the new update!\nCould not fetch info for {level}')
    except Exception as e:
        await interaction.channel.send("Couldn't fetch levels for user:" + " " + username)
client.run(constants.token)
