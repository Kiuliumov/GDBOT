from GDBOT.client import gd_client

class User:

    def __init__(self, username, password, discord_id: str):
        self.discord_id = discord_id
        self.username = username
        self.password = password
        self._logging_error = None

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


    async def get_messages(self):

        await self.__login()
        return await gd_client.get_messages()
