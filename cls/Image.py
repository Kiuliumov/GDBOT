from images import difficulty_images, emoji_ids


class Image:
    DIFFICULTY_IMAGES = difficulty_images.difficulty_images
    EMOJIS = emoji_ids.emojis

    def __init__(self, difficulty=None):
        self.difficulty = difficulty

    def get_image(self) -> str:
        return self.DIFFICULTY_IMAGES.get(self.difficulty,
                                          self.DIFFICULTY_IMAGES[
                                              'UNRATED' if 'DEMON' not in self.difficulty else 'HARD_DEMON'])

    def get_emoji(self, emoji_type):
        if emoji_type not in self.EMOJIS:
            print('Emoji not found.')
        else:
            return self.EMOJIS[emoji_type]
