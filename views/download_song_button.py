import discord
from GDBOT.client import gd_client
from GDBOT.src.Utils import Utils

class Download(discord.ui.View):
    def __init__(self, *, timeout=180, song_id):
        self.song_id = song_id
        super().__init__(timeout=timeout)

    @discord.ui.button(label="Download", style=discord.ButtonStyle.green)
    async def download(self, interaction: discord.Interaction, button: discord.ui.Button):
        song = await gd_client.get_song(self.song_id)
        embed = discord.Embed(color=Utils.generate_random_hex_int())
        embed.set_author(name=song.name)
        embed.set_thumbnail(url='https://uxwing.com/wp-content/themes/uxwing/download/web-app-development/download-round-color-blue-icon.png')
        embed.add_field(name='Download from here:', value=song.download_url)
        await interaction.response.send_message(embed=embed)
