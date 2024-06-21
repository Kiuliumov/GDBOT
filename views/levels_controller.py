import discord
from GDBOT.client import gd_client
from GDBOT.src.Builders import Builder
from GDBOT.src.Loader import Loader

class Controller(discord.ui.View):
    def __init__(self, *, timeout=180, level_ids):
        super().__init__(timeout=timeout)
        self.level_ids = level_ids
        self.current_index = 0

    @discord.ui.button(label='', style=discord.ButtonStyle.green, emoji='<:arrowleft:1210243998384652308> ')
    async def prev_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            self.current_index = (self.current_index - 1) % len(self.level_ids)
            level_id = self.level_ids[self.current_index]
            embed = await Builder.make_level_embed(level_id)
            embed.set_author(name=f'Level {self.current_index + 1} out of {len(self.level_ids)}')
            await interaction.response.edit_message(embed=embed)
        except Exception:
            await self.handle_error(interaction)

    @discord.ui.button(label='', style=discord.ButtonStyle.green, emoji='<:arrowright:1210243999982682173>  ')
    async def next_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            self.current_index = (self.current_index + 1) % len(self.level_ids)
            level_id = self.level_ids[self.current_index]
            embed = await Builder.make_level_embed(level_id)
            embed.set_author(name=f'Level {self.current_index + 1} out of {len(self.level_ids)}')
            await interaction.response.edit_message(embed=embed)
        except Exception:
            await self.handle_error(interaction)

    @discord.ui.button(label="Creator", style=discord.ButtonStyle.green)
    async def creator(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            level: gd_client.Level = await gd_client.get_level(level_id=self.level_ids[self.current_index])
            creator = level.creator
            embed = await Builder().make_user_embed(creator)
            await interaction.response.send_message(embed=embed)
        except Exception:
            await self.handle_error(interaction)

    @discord.ui.button(label="Get Song", style=discord.ButtonStyle.green)
    async def get_song(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            level: gd_client.Level = await gd_client.get_level(level_id=self.level_ids[self.current_index])
            song_id = level.song.id
            embed = await Builder().make_song_embed(song_id)
            await interaction.response.send_message(embed=embed, view=Download(song_id=song_id))
        except Exception:
            await self.handle_error(interaction)

    @discord.ui.button(label="Load Comments", style=discord.ButtonStyle.green)
    async def load_comments(self, interaction: discord.Interaction, button: discord.ui.Button):
        level: gd_client.Level = await gd_client.get_level(level_id=self.level_ids[self.current_index])
        comments = await Loader.load_level_comments(level)
        embed = Builder.make_comments_embed(comments)
        comments_view = UserComments(comments=comments)
        await interaction.response.send_message(embed=embed,view=comments_view)

    async def handle_error(self, interaction: discord.Interaction):
        embed = discord.Embed(title='An error occurred!')
        await interaction.response.send_message(embed=embed)


