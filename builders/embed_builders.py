from client import gd_client
import discord
from utils.util_functions import Utils
from builders.image_processing import Image
from builders import constants

current_image = Image(constants.app_id)


class Builder:
    def __init__(self, app_id):
        self.app_id = app_id

    @staticmethod
    async def make_level_embed(level_id: int) -> discord.Embed:
        level = await gd_client.get_level(level_id)
        if level.stars == 10:
            image = Image.get_demon_image(difficulty=level.difficulty)
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
    async def make_song_embed(song_id: int) -> discord.Embed:
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
    async def make_user_embed(username) -> discord.Embed:
        user: gd_client.AbstractUser = await gd_client.search_user(username)
        embed = discord.Embed(color=Utils.generate_random_hex_int()).set_author(name=user.name)
        embed.set_thumbnail(
            url='https://images-eds-ssl.xboxlive.com/image?url=4rt9.lXDC4H_93laV1_eHM0OYfiFeMI2p9MWie0CvL99U4GA1gf6_kayTt_kBblFwHwo8BW8JXlqfnYxKPmmBaGbzz_YTm90RlqatdfM6i.KS85qWpz59Ng19gHw42IuA5zqiP5GSXgIcvyalSoGK8hTwL2jCqbv5wfAhim5cQA-&format=source')
        embed.add_field(name="Leaderboard rank", value=user.statistics.rank, inline=True)
        embed.add_field(name="Stars", value=user.statistics.stars)
        embed.add_field(name="Diamonds", value=user.statistics.diamonds)
        embed.add_field(name="Secret coins", value=user.statistics.secret_coins)
        embed.add_field(name="User coins", value=user.statistics.user_coins)
        embed.add_field(name="Demons", value=user.statistics.demons)
        if user.statistics.creator_points:
            embed.add_field(name="Creator Points", value=user.statistics.creator_points)
        embed.add_field(name="User ID", value=user.id)
        embed.set_footer(text=f"By the Cantina®")
        return embed
