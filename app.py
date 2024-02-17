# todo implement command handling and slash commands
# todo implement weekly demon command
# todo implement account searching system
# todo implement pack searching system
# todo process the token
import discord
from builders import embed_builders
from client import gd_client
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.playing, name="Geometry Dash")
    await client.change_presence(activity=activity, status=discord.Status.online)
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ping'):
        await message.channel.send('Pong!')

    elif message.content.startswith('$daily'):
        try:
            daily = await gd_client.get_daily()
            embed = await embed_builders.make_level_embed(daily.id)
            await message.channel.send(embed=embed)
        except Exception as e:
            await message.channel.send(f'An error has occurred!\n{str(e).capitalize()}')
    elif message.content.startswith('$weekly'):
        weekly = await gd_client.get_weekly()
        try:
            embed = await embed_builders.make_level_embed(weekly.id)
            await message.channel.send(embed=embed)
        except Exception as e:
            await message.channel.send(f'An error has occurred!\n{str(e).capitalize()}')
    elif message.content.startswith('$song'):
        try:
            embed = await embed_builders.make_song_embed(int(message.content.split()[1]))
            await message.channel.send(embed=embed)
        except Exception as e:
            await message.channel.send(f'An error has occurred!\n{str(e).capitalize()}')

    elif message.content.startswith('$search'):
        try:
            embed = await embed_builders.make_level_embed(int(message.content.split()[1]))
            await message.channel.send(embed=embed)
        except TypeError:
            await message.channel.send('Please provide a valid ID!')
        except Exception as e:
            await message.channel.send(f'An error has occurred!\n{str(e).capitalize()}')


client.run('Enter your token here!')
