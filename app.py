import discord
from discord.ext import commands
from client import gd_client
from src.Loader import Loader
from src.Builders import Builder
from src.Search import Search
from images import text_art
from constants import TOKEN, PREFIX
from src.Views import Download, Controller

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=PREFIX, intents=intents)


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
        builder = Builder(ID=daily.id)
        embed = await builder.make_level_embed()
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        await interaction.response.send_message(f'An error has occurred!\n{str(e).capitalize()}')


@client.tree.command(name='weekly', description='Get the weekly level in Geometry Dash')
async def weekly(interaction: discord.Interaction):
    try:
        weekly = await gd_client.get_weekly()
        builder = Builder(ID=weekly.id)
        embed = await builder.make_level_embed()
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        await interaction.response.send_message(f'An error has occurred!\n{str(e).capitalize()}')


@client.tree.command(name='song', description='Get information about a song in Geometry Dash')
async def song(interaction: discord.Interaction, song_id: int):
    try:
        embed = await Builder.make_song_embed(song_id)
        await interaction.response.send_message(embed=embed,view=Download(song_id=song_id))
    except Exception as e:
        await interaction.response.send_message(f'An error has occurred!\n{str(e).capitalize()}')


@client.tree.command(name='search', description='Search for a level in Geometry Dash')
async def search_level(interaction: discord.Interaction, name: str):
    try:
        level_ids = await Search.search_level(name)
        controller = Controller(level_ids=level_ids)
        builder = Builder()
        builder.id = level_ids[0]
        embed = await builder.make_level_embed()
        embed.set_author(name=f'Level 1 out of {len(level_ids)}')
        await interaction.response.send_message(embed=embed, view=controller)
        Controller.flag = True
    except Exception as e:
        await interaction.channel.send(f'An error has occurred!\n{str(e).capitalize()}')


@client.tree.command(name='find_user', description='Find a user in Geometry Dash')
async def find_user(interaction: discord.Interaction, username: str):
    try:
        builder = Builder(username=username)
        embed = await builder.make_user_embed()
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        await interaction.response.send_message(f'An error has occurred!\n{str(e).capitalize()}')


@client.tree.command(name='load_user_levels', description='Loads user comments to a certain depth.')
async def load_user_levels(interaction: discord.Interaction, username: str):
    try:
        loader = Loader(username)
        levels = await loader.load_levels()
        level_ids = [level.id for level in levels]
        controller = Controller(level_ids=level_ids)
        builder = Builder()
        builder.id = level_ids[0]
        embed = await builder.make_level_embed()
        embed.set_author(name=f'Level 1 out of {len(levels)}')
        await interaction.response.send_message(embed=embed, view=controller)
        Controller.flag = True
    except Exception as e:
        print(e)


client.run(TOKEN)
