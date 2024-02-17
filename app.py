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
            random_color = ''.join(["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])])
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
            await message.channel.send('An error has occurred!',str(e).capitalize())

client.run('Enter your token here!')
