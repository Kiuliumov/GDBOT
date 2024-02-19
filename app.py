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

builder = Builder(constants.app_id)
search = Search(constants.app_id)
loader = Loader(constants.app_id)

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
        for ID in level_ids:
            try:
                embed = await builder.make_level_embed(ID)
                await interaction.response.send_message(embed=embed)
            except Exception as e:
                await interaction.response.send_message(str(e))
    except Exception as e:
        await interaction.response.send_message(f'An error has occurred!\n{str(e).capitalize()}')

@client.tree.command(name='find_user', description='Find a user in Geometry Dash')
async def find_user(interaction: discord.Interaction, username: str):
    try:
        embed = await builder.make_user_embed(username)
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        await interaction.response.send_message(f'An error has occurred!\n{str(e).capitalize()}')
@client.tree.command(name='load_user_comments',description='Loads user comments to a certain depth.The default is 5 and the current max is 99')
async def load_user_comments(interaction: discord.Interaction,username: str,depth: int = None):
        comments = loader.load_comments(username)
        index = 0
        for index,comment in enumerate(comments):
            index += 1
            if index > depth or index > 10:
                break
            await builder.make_comments_embed(comment)
            await interaction.response.send_message(embed=embed)
client.run(constants.token)
