from client import gd_client


class Loader:

    def __init__(self, username):
        self.username = username

    async def load_levels(self):
        user: gd_client.AbstractUser = await gd_client.search_user(self.username)
        levels = await user.get_levels()
        return levels

    async def load_comments(self):
        user: gd_client.AbstractUser = await gd_client.search_user(self.username)
        comments = await user.get_comments()
        return comments

    @staticmethod
    async def load_level_comments(level):
        comments = await level.get_comments()
        return comments