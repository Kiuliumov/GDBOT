import unittest
from unittest.mock import MagicMock, AsyncMock
from discord import Interaction, Message
from GDBOT.app import client as Bot

class TestBot(unittest.IsolatedAsyncioTestCase):

    async def test_ping_command(self):
        bot = Bot()
        interaction = MagicMock(spec=Interaction)

        await bot.ping_command(interaction)

        interaction.response.send_message.assert_called_once_with('Pong!')

    async def test_ping_command_error(self):
        bot = Bot()
        interaction = MagicMock(spec=Interaction)
        interaction.response.send_message = AsyncMock(side_effect=Exception('Test error'))

        await bot.ping_command(interaction)

        interaction.response.send_message.assert_called_once_with('An error has occurred!\nTest error')

    async def test_daily_command(self):
        bot = Bot()
        interaction = MagicMock(spec=Interaction)
        gd_client = MagicMock()
        gd_client.get_daily = AsyncMock(return_value=MagicMock(id=123))

        with unittest.mock.patch('app.gd_client', gd_client):
            await bot.daily_command(interaction)

        gd_client.get_daily.assert_called_once()
        interaction.response.send_message.assert_called_once()

    async def test_daily_command_error(self):
        bot = Bot()
        interaction = MagicMock(spec=Interaction)
        gd_client = MagicMock()
        gd_client.get_daily = AsyncMock(side_effect=Exception('Test error'))
        interaction.response.send_message = AsyncMock()

        with unittest.mock.patch('app.gd_client', gd_client):
            await bot.daily_command(interaction)

        gd_client.get_daily.assert_called_once()
        interaction.response.send_message.assert_called_once_with('An error has occurred!\nTest error')

    async def test_weekly_command(self):
        bot = Bot()
        interaction = MagicMock(spec=Interaction)
        gd_client = MagicMock()
        gd_client.get_weekly = AsyncMock(return_value=MagicMock(id=456))

        with unittest.mock.patch('app.gd_client', gd_client):
            await bot.weekly_command(interaction)

        gd_client.get_weekly.assert_called_once()
        interaction.response.send_message.assert_called_once()

    async def test_weekly_command_error(self):
        bot = Bot()
        interaction = MagicMock(spec=Interaction)
        gd_client = MagicMock()
        gd_client.get_weekly = AsyncMock(side_effect=Exception('Test error'))
        interaction.response.send_message = AsyncMock()

        with unittest.mock.patch('app.gd_client', gd_client):
            await bot.weekly_command(interaction)

        gd_client.get_weekly.assert_called_once()
        interaction.response.send_message.assert_called_once_with('An error has occurred!\nTest error')

    async def test_song_command(self):
        bot = Bot()
        interaction = MagicMock(spec=Interaction)
        gd_client = MagicMock()
        gd_client.get_song = AsyncMock(return_value=MagicMock(download_url='https://example.com/song.mp3'))

        with unittest.mock.patch('app.gd_client', gd_client):
            await bot.song_command(interaction, 789)

        gd_client.get_song.assert_called_once_with(789)
        interaction.response.send_message.assert_called_once()

    async def test_song_command_error(self):
        bot = Bot()
        interaction = MagicMock(spec=Interaction)
        gd_client = MagicMock()
        gd_client.get_song = AsyncMock(side_effect=Exception('Test error'))
        interaction.response.send_message = AsyncMock()

        with unittest.mock.patch('app.gd_client', gd_client):
            await bot.song_command(interaction, 789)

        gd_client.get_song.assert_called_once_with(789)
        interaction.response.send_message.assert_called_once_with('An error has occurred!\nTest error')

    async def test_search_level_command(self):
        bot = Bot()
        interaction = MagicMock(spec=Interaction)
        Search = MagicMock()
        Search.search_level = AsyncMock(return_value=[123, 456, 789])
        Controller = MagicMock()
        controller_instance = MagicMock()
        Controller.return_value = controller_instance
        Builder = MagicMock()
        Builder.make_level_embed = AsyncMock(return_value=MagicMock())
        controller_instance.flag = True

        with unittest.mock.patch.multiple('app', Search=Search, Controller=Controller, Builder=Builder):
            await bot.search_level_command(interaction, 'test')

        Search.search_level.assert_called_once_with('test')
        Controller.assert_called_once_with(level_ids=[123, 456, 789])
        Builder.make_level_embed.assert_called_once_with(123)
        controller_instance.set_author.assert_called_once_with(name='Level 1 out of 3')
        interaction.response.send_message.assert_called_once()

    async def test_search_level_command_error(self):
        bot = Bot()
        interaction = MagicMock(spec=Interaction)
        Search = MagicMock()
        Search.search_level = AsyncMock(side_effect=Exception('Test error'))
        interaction.channel.send = AsyncMock()

        with unittest.mock.patch('app.Search', Search):
            await bot.search_level_command(interaction, 'test')

        Search.search_level.assert_called_once_with('test')
        interaction.channel.send.assert_called_once_with('An error has occurred!\nTest error')

    async def test_find_user_command_success(self):
        bot = Bot()
        interaction = MagicMock(spec=Interaction)
        Builder = MagicMock()
        Builder.make_user_embed = AsyncMock(return_value=MagicMock())

        with unittest.mock.patch('app.Builder', Builder):
            await bot.find_user_command(interaction, 'test')

        Builder.make_user_embed.assert_called_once_with('test')
        interaction.response.send_message.assert_called_once()
    async def test_find_user_command_error(self):
        bot = Bot()
        interaction = MagicMock(spec=Interaction)
        Builder = MagicMock()
        Builder.make_user_embed = AsyncMock(side_effect=Exception('Test error'))
        interaction.response.send_message = AsyncMock()

        with unittest.mock.patch('app.Builder', Builder):
            await bot.find_user_command(interaction, 'test')

        Builder.make_user_embed.assert_called_once_with('test')
        interaction.response.send_message.assert_called_once_with('An error has occurred!\nTest error')
    async def test_load_user_levels_command_success(self):
        bot = Bot()
        interaction = MagicMock(spec=Interaction)
        Loader = MagicMock()
        loader_instance = MagicMock()
        Loader.return_value = loader_instance
        loader_instance.load_levels = AsyncMock(return_value=[MagicMock(id=123), MagicMock(id=456)])
        Controller = MagicMock()
        controller_instance = MagicMock()
        Controller.return_value = controller_instance
        Builder = MagicMock()
        Builder.make_level_embed = AsyncMock(return_value=MagicMock())

        with unittest.mock.patch.multiple('app', Loader=Loader, Controller=Controller, Builder=Builder):
            await bot.load_user_levels_command(interaction, 'test')
        Loader.assert_called_once_with('test')
        loader_instance.load_levels.assert_called_once()
        Controller.assert_called_once_with(level_ids=[123, 456])
        Builder.make_level_embed.assert_called_once_with(123)
        controller_instance.set_author.assert_called_once_with(name='Level 1 out of 2')
        interaction.response.send_message.assert_called_once()
    async def test_load_comments_command_success(self):
        bot = Bot()
        interaction = MagicMock(spec=Interaction)
        Loader = MagicMock()
        loader_instance = MagicMock()
        Loader.return_value = loader_instance
        comments = [MagicMock(), MagicMock(), MagicMock()]
        loader_instance.load_comments = AsyncMock(return_value=comments)
        UserComments = MagicMock()
        comments_instance = MagicMock()
        UserComments.return_value = comments_instance
        Builder = MagicMock()
        Builder.make_comments_embed = AsyncMock(return_value=MagicMock())
        with unittest.mock.patch.multiple('app', Loader=Loader, UserComments=UserComments, Builder=Builder):
            await bot.load_comments_command(interaction, 'test')
        Loader.assert_called_once_with('test')
        loader_instance.load_comments.assert_called_once()
        UserComments.assert_called_once_with(comments=comments)
        Builder.make_comments_embed.assert_called_once_with(comments[0])
        interaction.response.send_message.assert_called_once()

