from client import gd_client
import discord
from src.Utils import Utils
from src.Image import Image
from src.Emoji import Emoji

class Builder:
    @staticmethod
    async def make_level_embed(id):
        level = await gd_client.get_level(id)
        image = Image(str(level.difficulty)[11:]).get_image()
        embed = discord.Embed(title=level, color=Utils.generate_random_hex_int())
        embed.set_thumbnail(url=image)
        embed.add_field(name='Description:', value=level.description, inline=True)
        embed.add_field(name='Version', value=level.version)
        if level.stars:
            embed.add_field(name='Stars', value=level.stars)
        else:
            embed.add_field(name='Stars', value='Level is not rated!')
        embed.add_field(name='Downloads', value=level.downloads)
        embed.add_field(name='Likes', value=level.rating)
        embed.add_field(name='Creator', value=level.creator)
        embed.add_field(name='Song', value=level.song)
        return embed

    @staticmethod
    async def make_song_embed(id):
        song = await gd_client.get_song(id)
        embed = discord.Embed(color=Utils.generate_random_hex_int()).set_author(name=song.name)
        embed.set_thumbnail(url='https://i.redd.it/r30pn3cei4r81.png')
        embed.add_field(name="Song author", value=song.artist.name)
        embed.add_field(name="Song ID", value=song.id)
        embed.add_field(name="Song size", value=song.size)
        embed.add_field(name="Link", value=song.url)
        embed.set_footer(text=f"By the Cantina®")
        return embed

    @staticmethod
    async def make_user_embed(username):
        user: gd_client.AbstractUser = await gd_client.search_user(username)
        if user.statistics.rank == 0:
            user.statistics.rank = 'This user is banned from the leaderboards!'
        embed = discord.Embed(color=Utils.generate_random_hex_int()).set_author(name=user.name)
        embed.set_thumbnail(
            url='https://gdbrowser.com/assets/search-user.png')
        embed.add_field(name="Leaderboard rank " + Emoji.emojis['LeaderboardTrophy01'], value=user.statistics.rank,
                        inline=True)
        embed.add_field(name="Stars " + Emoji.emojis['Star'], value=user.statistics.stars)
        embed.add_field(name="Diamonds " + Emoji.emojis['Diamond'], value=user.statistics.diamonds)
        embed.add_field(name="Secret coins " + Emoji.emojis['Secret_coin'], value=user.statistics.secret_coins)
        embed.add_field(name="User coins " + Emoji.emojis['UserCoin'], value=user.statistics.user_coins)
        embed.add_field(name="Demons " + Emoji.emojis['Demon'], value=user.statistics.demons)
        return embed

    @staticmethod
    def make_comments_embed(comment):
        embed = discord.Embed(color=Utils.generate_random_hex_int()).set_author(name=comment.author.name)
        embed.add_field(name=comment.content, value=str(comment.rating) + Emoji.emojis['Like'],inline=True)
        embed.set_footer(text='By ' + comment.author.name +'      Created at: ' + str(comment.created_at)[:11])
        return embed
