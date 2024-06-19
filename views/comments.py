from __init__ import *

class UserComments(discord.ui.View):
    def __init__(self, *, timeout=180, comments):
        super().__init__(timeout=timeout)
        self.comments = comments
        self.index = 0

    @discord.ui.button(label='', style=discord.ButtonStyle.green, emoji='<:arrowleft:1210243998384652308> ')
    async def prev_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            self.index = self.index - 1
            if self.index < 0:
                self.index = len(self.comments) - 1
            comment = self.comments[self.index]
            embed = Builder.make_comments_embed(comment)
            embed.set_author(name=f'Comment {self.index + 1} out of {len(self.comments)}')
            await interaction.response.edit_message(embed=embed)
        except Exception:
            await self.handle_error(interaction)


    @discord.ui.button(label='', style=discord.ButtonStyle.green, emoji='<:arrowright:1210243999982682173>')
    async def next_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            self.index = self.index + 1
            if self.index == len(self.comments):
                self.index = 0
            comment = self.comments[self.index]
            embed = Builder.make_comments_embed(comment)
            embed.set_author(name=f'Comment {self.index + 1} out of {len(self.comments)}')
            await interaction.response.edit_message(embed=embed)
        except Exception:
            await self.handle_error(interaction)

    async def handle_error(self, interaction: discord.Interaction):
        embed = discord.Embed(title='An error occurred!')
        await interaction.response.send_message(embed=embed)
