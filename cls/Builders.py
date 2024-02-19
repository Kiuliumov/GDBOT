from client import gd_client
import discord
from cls.Utils import Utils
from cls.Image import Image
from constants import app_id
current_image = Image(app_id)


class Builder:
    def __init__(self, app_id):
        self.app_id = app_id

    @staticmethod
    async def make_level_embed(level_id: int):
        level = await gd_client.get_level(level_id)
        if level.stars == 10:
            image = current_image.get_demon_image(difficulty=level.difficulty)
        else:
            image = current_image.get_image(difficulty=level.difficulty)
        embed = discord.Embed(color=Utils.generate_random_hex_int()).set_author(name=level)
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

    @staticmethod
    async def make_song_embed(song_id: int):
        song = await gd_client.get_song(song_id)
        embed = discord.Embed(color=Utils.generate_random_hex_int()).set_author(name=song.name)
        embed.set_thumbnail(url='https://i.redd.it/r30pn3cei4r81.png')
        embed.add_field(name="Song author", value=song.artist.name)
        embed.add_field(name="Song ID", value=song.id)
        embed.add_field(name="Song size", value=song.size)
        embed.add_field(name="Link", value=song.url)
        embed.set_footer(text=f"By the Cantina®")
        return embed

    @staticmethod
    async def make_comments_embed(comment):
        embed = discord.Embed(color=Utils.generate_random_hex_int()).set_author(name=comment.author)
        embed.description(comment.body)
        embed.set_footer(comment.timestamp)
