import discord
from client import gd_client
from cls.Utils import Utils


class Download(discord.ui.View):
    song_id = None

    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
        self.clicked = False

    @discord.ui.button(label="Download", style=discord.ButtonStyle.green)
    async def gray_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not self.clicked:
            song = await gd_client.get_song(Download.song_id)
            embed = discord.Embed(color=Utils.generate_random_hex_int()).set_author(name=song.name)
            embed.set_thumbnail(
                url='https://uxwing.com/wp-content/themes/uxwing/download/web-app-development/download-round-color-blue-icon.png')
            embed.add_field(name='Download from here:', value=song.download_url)
            await interaction.response.send_message(embed=embed)
