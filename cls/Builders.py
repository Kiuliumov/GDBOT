from client import gd_client
import discord
from cls.Utils import Utils
from cls.Image import Image


class Builder:
    def __init__(self, username='', ID=0):
        self.id = int(ID)
        self.username = username

    async def make_level_embed(self):
        level = await gd_client.get_level(self.id)
        image = Image(level.difficulty[11:]).get_image()
        embed = discord.Embed(color=Utils.generate_random_hex_int()).set_author(name=level)
        embed.set_thumbnail(url=image)
        embed.add_field(name='Description:', value=level.description, inline=True)
        embed.add_field(name='Version', value=level.version)
        if level.stars:
            embed.add_field(name='Stars', value=level.stars)
        else:
            embed.add_field(name='Stars', value='Level is not rated!')
        embed.add_field(name='Downloads', value=level.downloads)
        embed.add_field(name='Version', value=level.rating)
        embed.add_field(name='Creator', value=level.creator)
        embed.add_field(name='Song', value=level.song)
        embed.set_footer(text=f"By the Cantina®")
        return embed

    async def make_song_embed(self):
        song = await gd_client.get_song(self)
        embed = discord.Embed(color=Utils.generate_random_hex_int()).set_author(name=song.name)
        embed.set_thumbnail(url='https://i.redd.it/r30pn3cei4r81.png')
        embed.add_field(name="Song author", value=song.artist.name)
        embed.add_field(name="Song ID", value=song.id)
        embed.add_field(name="Song size", value=song.size)
        embed.add_field(name="Link", value=song.url)
        embed.set_footer(text=f"By the Cantina®")
        return embed

    async def make_user_embed(self) -> discord.Embed:
        user: gd_client.AbstractUser = await gd_client.search_user(self.username)
        embed = discord.Embed(color=Utils.generate_random_hex_int()).set_author(name=user.name)
        embed.set_thumbnail(
            url='https://images-eds-ssl.xboxlive.com/image?url=4rt9'
                '.lXDC4H_93laV1_eHM0OYfiFeMI2p9MWie0CvL99U4GA1gf6_kayTt_kBblFwHwo8BW8JXlqfnYxKPmmBaGbzz'
                '_YTm90RlqatdfM6i.KS85qWpz59Ng19gHw42IuA5zqiP5GSXgIcvyalSoGK8hTw'
                'L2jCqbv5wfAhim5cQA-&format=source')
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
