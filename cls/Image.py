from images.difficulty_images import DICT_OF_IMAGES


class Image:
    DIFFICULTY_IMAGES = DICT_OF_IMAGES

    def __init__(self, difficulty):
        self.difficulty = difficulty

    def get_image(self) -> str:
        return self.DIFFICULTY_IMAGES.get(self.difficulty,
                                          self.DIFFICULTY_IMAGES[
                                              'UNRATED' if 'DEMON' not in self.difficulty else 'HARD_DEMON'])
