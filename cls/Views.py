import discord
from client import gd_client
from cls.Utils import Utils
from cls.Builders import Builder

class Download(discord.ui.View):
    song_id = None

    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)

    @discord.ui.button(label="Download", style=discord.ButtonStyle.green)
    async def gray_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        song = await gd_client.get_song(Download.song_id)
        embed = discord.Embed(color=Utils.generate_random_hex_int()).set_author(name=song.name)
        embed.set_thumbnail(
            url='https://uxwing.com/wp-content/themes/uxwing/download/web-app-development/download-round-color-blue-icon.png')
        embed.add_field(name='Download from here:', value=song.download_url)
        await interaction.response.send_message(embed=embed)


class Controller(discord.ui.View):
    level_ids = None
    flag = False
    current_index = 0 if flag else 1
    song_id = None
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)

    @discord.ui.button(label='', style=discord.ButtonStyle.green, emoji='<:arrowleft:1210243998384652308> ')
    async def prev_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if Controller.current_index - 1 < 0:
            Controller.current_index = len(Controller.level_ids) - 1
        level_id = Controller.level_ids[Controller.current_index]
        embed = await Builder(ID=level_id).make_level_embed()
        embed.set_author(name=f'Level {Controller.current_index - 1} out of {len(Controller.level_ids)}')
        await interaction.response.edit_message(embed=embed)
        Controller.current_index -= 1

    @discord.ui.button(label='', style=discord.ButtonStyle.green, emoji='<:arrowright:1210243999982682173>  ')
    async def next_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if Controller.current_index + 1 > len(Controller.level_ids):
            Controller.current_index = 0
        level_id = Controller.level_ids[Controller.current_index]
        embed = await Builder(ID=level_id).make_level_embed()
        embed.set_author(name=f'Level {Controller.current_index + 1} out of {len(Controller.level_ids)}')
        await interaction.response.edit_message(embed=embed)
        Controller.current_index += 1

    @discord.ui.button(label="Add bot", style=discord.ButtonStyle.green)
    async def add_bot(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Under construction!')

    @discord.ui.button(label="The Cantina", style=discord.ButtonStyle.green)
    async def server(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Under construction!')

    @discord.ui.button(label="GitHub Repository", style=discord.ButtonStyle.green)
    async def github(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Under construction!')