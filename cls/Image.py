from images import difficulty_images,emojis


class Image:
    DIFFICULTY_IMAGES = difficulty_images.difficulty_images
    EMOJIS = emojis.emojis

    def __init__(self, difficulty):
        self.difficulty = difficulty

    def get_image(self) -> str:
        return self.DIFFICULTY_IMAGES.get(self.difficulty,
                                          self.DIFFICULTY_IMAGES[
                                              'UNRATED' if 'DEMON' not in self.difficulty else 'HARD_DEMON'])
