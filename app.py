# todo implement command handling and slash commands
# todo implement weekly demon command
# todo implement level searching based on id or level name
# todo implement account searching system
# todo implement pack searching system
# todo process the token
import discord
import gd
from utils import util_functions
import random
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
gd_client = gd.Client()

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
        daily = await gd_client.get_daily()
        image = util_functions.get_image(daily.stars)
        embed = discord.Embed(color=util_functions.generate_random_hex_int()).set_author(name="Current Daily")
        embed.set_thumbnail(url=image)
        embed.add_field(name="Name", value=daily.name)
        embed.add_field(name="Difficulty", value=f"{daily.stars} stars")
        embed.add_field(name="ID", value=f"{daily.id}")
        embed.set_footer(text=f"Creator: {daily.creator.name}")
        await message.channel.send(embed=embed)

    elif message.content.startswith('$song'):
        try:
            song_id = message.content.split()[1]
            song = await gd_client.get_song(song_id)
            embed = discord.Embed(color=util_functions.generate_random_hex_int()).set_author(name=song.name)
            embed.set_thumbnail(url='https://i.redd.it/r30pn3cei4r81.png')
            embed.add_field(name="Song author", value=song.artist.name)
            embed.add_field(name="Song ID", value=song.id)
            embed.add_field(name="Song size", value=song.size)
            embed.add_field(name="Link", value=song.url)
            embed.set_footer(text=f"By the Cantina®")
            await message.channel.send(embed=embed)
        except Exception as e:
            await message.channel.send(f'An error has occurred!\n{str(e).capitalize()}')
    elif message.content.startswith('$search'):
        try:
            level_name = message.content.split()[1]
            if len(message.content.split()) <= 2:
                n = 5
            else:
                n = int(message.content.split()[2])
            for counter,level in enumerate(await gd_client.search_levels(level_name)):
                counter += 1
                if counter >= n or counter >= 99:
                    break
                await message.channel.send(level)
        except IndexError:
            await message.channel.send('Provide level name and depth in this format:\n$search level_name depth')
        except Exception as e:
            await message.channel.send(f'An error has occurred!\n{str(e).capitalize()}')


client.run('MTIwODM5Mjk4OTY1MTc2MzI0MA.G3vPyH.r9vL_bjTRaENl_gooMr_5taHZAK-YvfviVKP_A')
