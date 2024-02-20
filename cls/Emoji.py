from cls.Image import Image

image = Image()


class Emoji:
    def __init__(self):
        self.diamond = image.get_emoji('Diamond')
        self.leaderboard_1 = image.get_emoji('LeaderboardTrophy01')
        self.leaderboard_2 = image.get_emoji('LeaderboardTrophy02')
        self.leaderboard_3 = image.get_emoji('LeaderboardTrophy03')
        self.leaderboard_4 = image.get_emoji('LeaderboardTrophy04')
        self.secret_coin = image.get_emoji('Secret_coin')
        self.user_coin = image.get_emoji('Like')
        self.star = image.get_emoji('Star')
        self.download_symbol = image.get_emoji('Download_symbol')
        self.like = image.get_emoji('Like')
        self.creator_points = image.get_emoji('CreatorPoints')
