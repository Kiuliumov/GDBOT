import discord
from client import gd_client
from builders.embed_builders import Builder
from builders.constants import token, prefix, app_id

intents = discord.Intents.default()
client = discord.Client(intents=intents)

builder = Builder(app_id)


@client.event
async def on_ready():
    print(client.user)
    print(client.user.id)
    print('------------------------------')
    try:
        activity = discord.Activity(type=discord.ActivityType.playing, name="Geometry Dash")
        await client.change_presence(activity=activity, status=discord.Status.online)
    except Exception as e:
        print(e)


@client.event
async def on_message(message):
    if message.author == client.user:
        return


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ping'):
        await message.channel.send('Pong!')

    elif message.content.startswith('$daily'):
        try:
            daily = await gd_client.get_daily()
            embed = await builder.make_level_embed(daily.id)
            await message.channel.send(embed=embed)
        except Exception as e:
            await message.channel.send(f'An error has occurred!\n{str(e).capitalize()}')
    elif message.content.startswith('$weekly'):
        weekly = await gd_client.get_weekly()
        try:
            embed = await builder.make_level_embed(weekly.id)
            await message.channel.send(embed=embed)
        except Exception as e:
            await message.channel.send(f'An error has occurred!\n{str(e).capitalize()}')
    elif message.content.startswith('$song'):
        try:
            embed = await builder.make_song_embed(int(message.content.split()[1]))
            await message.channel.send(embed=embed)
        except Exception as e:
            await message.channel.send(f'An error has occurred!\n{str(e).capitalize()}')

    elif message.content.startswith('$search'):
        try:
            embed = await builder.make_level_embed(int(message.content.split()[1]))
            await message.channel.send(embed=embed)
        except TypeError:
            await message.channel.send('Please provide a valid ID!')
        except Exception as e:
            await message.channel.send(f'An error has occurred!\n{str(e).capitalize()}')


client.run(token)
