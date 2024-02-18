from client import gd_client
import discord
from utils.util_functions import generate_random_hex_int
from builders.image_processing import Image
current_image = Image()
class Builder():
    def __init__(self):
        pass

    async def make_level_embed(self,level_id: int):
        level = await gd_client.get_level(level_id)
        if level.stars == 10:
            image = current_image.get_demon_image(difficulty=level.difficulty)
        else:
            image = current_image.get_image(difficulty=level.difficulty)
        embed = discord.Embed(color=generate_random_hex_int()).set_author(name=level)
        embed.set_thumbnail(url=image)
        embed.add_field(name='Description:', value=level.description, inline=True)
        embed.add_field(name='Version', value=level.version)
        embed.add_field(name='Stars', value=level.stars)
        embed.add_field(name='Downloads', value=level.downloads)
        embed.add_field(name='Version', value=level.rating)
        embed.add_field(name='Creator', value=level.creator)
        embed.add_field(name='Song', value=level.song)
        embed.set_footer(text=f"By the Cantina®")
        return embed


    async def make_song_embed(self,song_id: int):
        song = await gd_client.get_song(song_id)
        embed = discord.Embed(color=generate_random_hex_int()).set_author(name=song.name)
        embed.set_thumbnail(url='https://i.redd.it/r30pn3cei4r81.png')
        embed.add_field(name="Song author", value=song.artist.name)
        embed.add_field(name="Song ID", value=song.id)
        embed.add_field(name="Song size", value=song.size)
        embed.add_field(name="Link", value=song.url)
        embed.set_footer(text=f"By the Cantina®")
        return embed
