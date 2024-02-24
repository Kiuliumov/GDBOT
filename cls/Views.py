import discord
from client import gd_client
from cls.Builders import Builder
from cls.Utils import Utils

class Download(discord.ui.View):
    def __init__(self, *, timeout=180, song_id):
        self.song_id = song_id
        super().__init__(timeout=timeout)

    @discord.ui.button(label="Download", style=discord.ButtonStyle.green)
    async def download(self, interaction: discord.Interaction, button: discord.ui.Button):
        song = await gd_client.get_song(self.song_id)

        embed = discord.Embed(color=Utils.generate_random_hex_int())
        embed.set_author(name=song.name)
        embed.set_thumbnail(
            url='https://uxwing.com/wp-content/themes/uxwing/download/web-app-development/download-round-color-blue-icon.png')
        embed.add_field(name='Download from here:', value=song.download_url)
        await interaction.response.send_message(embed=embed)


class Controller(discord.ui.View):

    def __init__(self, *, timeout=180, level_ids):
        super().__init__(timeout=timeout)
        self.level_ids = level_ids
        flag = False
        self.current_index = 0
        song_id = None

    @discord.ui.button(label='', style=discord.ButtonStyle.green, emoji='<:arrowleft:1210243998384652308> ')
    async def prev_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            if self.current_index == 0:
                self.current_index = len(self.level_ids) - 1
            else:
                self.current_index -= 1

            level_id = self.level_ids[self.current_index]
            embed = await Builder(ID=level_id).make_level_embed()
            embed.set_author(name=f'Level {self.current_index + 1} out of {len(self.level_ids)}')
            await interaction.response.edit_message(embed=embed)
        except Exception:
            await interaction.response.edit_message('Gd.py is not up to date!')

    @discord.ui.button(label='', style=discord.ButtonStyle.green, emoji='<:arrowright:1210243999982682173>  ')
    async def next_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            if self.current_index == len(self.level_ids) - 1:
                self.current_index = 0
            else:
                self.current_index += 1

            level_id = self.level_ids[self.current_index]
            embed = await Builder(ID=level_id).make_level_embed()
            embed.set_author(name=f'Level {self.current_index + 1} out of {len(self.level_ids)}')
            await interaction.response.edit_message(embed=embed)
        except Exception:
            await interaction.response.edit_message('Try again!')

    @discord.ui.button(label="Get Song", style=discord.ButtonStyle.green)
    async def add_bot(self, interaction: discord.Interaction, button: discord.ui.Button):
        level: gd_client.Level = await gd_client.get_level(level_id=self.level_ids[self.current_index])
        song_id = level.song.id
        embed = await Builder(ID=song_id).make_song_embed()
        await interaction.response.send_message(embed=embed, view=Download(song_id=song_id))

    @discord.ui.button(label="The Cantina", style=discord.ButtonStyle.green)
    async def server(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Under construction!')

    @discord.ui.button(label="GitHub Repository", style=discord.ButtonStyle.green)
    async def github(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(color=Utils.generate_random_hex_int())
        embed.add_field(name='GitHub',value='https://github.com/Kiuliumov/GDBOT')
        embed.set_thumbnail(url='https://cdn-icons-png.flaticon.com/512/25/25231.png')
        await interaction.response.send_message(embed=embed)
