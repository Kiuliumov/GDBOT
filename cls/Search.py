from client import gd_client


class Search:

    @staticmethod
    async def search_level(name: str) -> list:
        level_ids = []
        for i, level in enumerate(await gd_client.search_levels(name)):
            level_ids.append(level.id)
        return level_ids

    @staticmethod
    async def search_for_user(name: str) -> int:
        name = name.strip()
        user: gd_client.AbstractUser = await gd_client.search_user(name)
        return int(user.id)
