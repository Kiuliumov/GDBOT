import discord
from GDBOT.client import gd_client
from src.Loader import Loader
from src.Builders import Builder
from src.Search import Search
from images import text_art
from constants import TOKEN, PREFIX
from views.comments import UserComments
from views.download_song_button import Download
from views.levels_controller import Controller
from client import client
from user.user import User




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
        embed = await Builder.make_level_embed(daily.id)
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        await interaction.response.send_message(f'An error has occurred!\n{str(e).capitalize()}')


@client.tree.command(name='weekly', description='Get the weekly level in Geometry Dash')
async def weekly(interaction: discord.Interaction):
    try:
        weekly = await gd_client.get_weekly()
        embed = await Builder.make_level_embed(weekly.id)
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        await interaction.response.send_message(f'An error has occurred!\n{str(e).capitalize()}')


@client.tree.command(name='song', description='Get information about a song in Geometry Dash')
async def song(interaction: discord.Interaction, song_id: int):
    try:
        embed = await Builder.make_song_embed(song_id)
        await interaction.response.send_message(embed=embed, view=Download(song_id=song_id))
    except Exception as e:
        await interaction.response.send_message(f'An error has occurred!\n{str(e).capitalize()}')


@client.tree.command(name='search', description='Search for a level in Geometry Dash')
async def search_level(interaction: discord.Interaction, name: str):
    try:
        level_ids = await Search.search_level(name)
        controller = Controller(level_ids=level_ids)
        embed = await Builder.make_level_embed(level_ids[0])
        embed.set_author(name=f'Level 1 out of {len(level_ids)}')
        await interaction.response.send_message(embed=embed, view=controller)
        Controller.flag = True
    except Exception as e:
        await interaction.channel.send(f'An error has occurred!\n{str(e).capitalize()}')


@client.tree.command(name='find_user', description='Find a user in Geometry Dash')
async def find_user(interaction: discord.Interaction, username: str):

    try:
        embed = await Builder.make_user_embed(username)
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
        embed = await Builder.make_level_embed(level_ids[0])
        embed.set_author(name=f'Level 1 out of {len(levels)}')
        await interaction.response.send_message(embed=embed, view=controller)
        Controller.flag = True
    except IndexError:
        try:
            embed = discord.Embed(
                title=f'WE CAN\'T GET THIS LEVEL,BECAUSE GD.PY IS NOT UP TO DATE! `id:{level_ids[0]}`')
            await interaction.response.send_message(embed=embed, view=controller)
        except Exception:
            embed = discord.Embed(
                title=f'`We cannot find user with name:{username}`')
            await interaction.response.send_message(embed=embed)


@client.tree.command(name='load_profile_comments', description='Loads the comments of a user!')
async def load_profile_comments(interaction: discord, username: str):
    try:
        loader = Loader(username)
        comments = await loader.load_comments()
        comments_view = UserComments(comments=comments)
        embed = Builder.make_comments_embed(comments[0])
        embed.set_author(name=f'Comment 1 out of {len(comments)}')
        await interaction.response.send_message(embed=embed, view=comments_view)
    except discord.app_commands.errors.CommandInvokeError:
        embed = discord.Embed(
            title=f'`We cannot find user with name:{username}`')
        await interaction.response.send_message(embed=embed)

@client.tree.command(name='login', description='Login into your geometry dash account!')
async def login(interaction: discord.Interaction, username: str, password: str):
    user = await User.create_user(str(interaction.user.id), username, password)

    if user is None:
        return 'Login failed. Please try again.'

    return 'Logged in successfully.'

@client.tree.command(name='get_chests', description='Gets the chests for a given user! Requires login!')
async def get_chests(interaction: discord.Interaction):

    user = User.get_user(str(interaction.user.id))

    if not user:
        await interaction.response.send_message('You need to log in first!')

    await interaction.user.send_message(user.get_chests())


client.run(TOKEN)