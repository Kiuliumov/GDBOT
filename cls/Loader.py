from client import gd_client


class Loader:

    @staticmethod
    async def load_levels(username):
        user: gd_client.AbstractUser = await gd_client.search_user(username)
        levels = await user.get_levels()
        return levels

    @staticmethod
    async def load_comments(username):
        user: gd_client.AbstractUser = await gd_client.search_user(username)
        comments = await user.get_comments()
        return comments

