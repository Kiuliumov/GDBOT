import discord
import gd
from utils.get_image import get_image

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
        image = get_image(daily.stars)
        embed = discord.Embed(color=0x7289da).set_author(name="Current Daily")
        embed.set_image(url=image)
        embed.add_field(name="Name", value=daily.name)
        embed.add_field(name="Difficulty", value=f"{daily.stars} stars")
        embed.add_field(name="ID", value=f"{daily.id}")
        embed.set_footer(text=f"Creator: {daily.creator.name}")
        await message.channel.send(embed=embed)

client.run()
