import discord
from discord.ext import commands
from client import gd_client
from cls.Builders import Builder
from cls.Search import Search
from images import text_art
from constants import TOKEN, PREFIX
from cls.Views import Download
from cls.Utils import Utils

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
        current_song_download_url = await gd_client.get_song(song_id)
        current_song_download_url = current_song_download_url.download_url
        await interaction.response.send_message(embed=embed,view=Download())
        Download.song_id = song_id
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
        builder = Builder()
        for ID in level_ids:
            builder.id = ID
            embed = await builder.make_level_embed()
            await interaction.channel.send(embed=embed)
            await interaction.channel.send('----------------------------------------------------------------------------------------------------------')
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


@client.tree.command(name='load_user_levels',description='Loads user comments to a certain depth.')
async def load_user_levels(interaction: discord.Interaction,username: str,depth: int = 5):
    try:
        levels = await loader.load_levels(username)
        await interaction.response.send_message(f"{username}'s levels:")
        builder = Builder()
        for index,level in enumerate(levels):
            index += 1
            if index > depth or index > 50:
                break
            try:
                builder.id = level.id
                embed = await builder.make_level_embed()
                await interaction.channel.send('----------------------------------------------------------------------------------------------------------')
                await interaction.channel.send(embed=embed)
            except Exception as e:
                await interaction.channel.send(f'gd.py is still outdated for levels from the new update!\nCould not fetch info for {level}')
    except Exception as e:
        await interaction.response.send_message("Couldn't fetch levels for user:" + " " + username)

client.run(TOKEN)
