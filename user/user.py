import gd
import dbconfig
from GDBOT.client import gd_client


class User:
    REGISTERED_USERS = []

    def __init__(self, discord_id: str):
        dbconfig.create_table()
        self.id = discord_id

    @property
    def username(self):
        user = dbconfig.fetch_user(self.id)
        if user is None:
            raise ValueError("User not found")
        return user['username']

    @property
    def password(self):
        user = dbconfig.fetch_user(self.id)
        if user is None:
            raise ValueError("User not found")
        return user['password']

    async def __login(self):
        try:
            await gd_client.login(self.username, self.password)
        except Exception as error:
            self._logging_error = error

    async def get_quests(self):

        await self.__login()
        return await gd_client.get_quests()

    async def get_chests(self):

        await self.__login()
        return await gd_client.get_chests()

    async def get_friend_requests(self):

        await self.__login()
        return await gd_client.get_friend_requests()

    async def get_comments(self):

        await self.__login()
        return await gd_client.get_comments()

    @classmethod
    async def create_user(cls, discord_id: str, username: str, password: str):

        try:
            await gd_client.login(username, password)
        except gd.LoginFailed:
            return None

        dbconfig.insert_user(discord_id, username, password)

        return cls(discord_id)

    @staticmethod
    def get_user(discord_id: str):
        for user in User.REGISTERED_USERS:
            if user.id == discord_id:
                return user
