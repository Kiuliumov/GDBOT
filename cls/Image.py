class Image:
    DIFFICULTY_IMAGES = {
        'AUTO': 'https://static.wikia.nocookie.net/geometry-dash/images/e/e8/Auto.png/revision/latest/scale-to-width-down/1000?cb=20240128012123',
        'EASY': 'https://static.wikia.nocookie.net/geometry-dash/images/7/7a/Easy.png/revision/latest/scale-to-width-down/1000?cb=20240128012431',
        'NORMAL': 'https://static.wikia.nocookie.net/geometry-dash/images/f/fb/Normal.png/revision/latest/scale-to-width-down/1000?cb=20231027082451',
        'HARD': 'https://static.wikia.nocookie.net/geometry-dash/images/d/d5/Hard.png/revision/latest/scale-to-width-down/1000?cb=20240128012620',
        'HARDER': 'https://static.wikia.nocookie.net/geometry-dash/images/d/db/Harder.png/revision/latest/scale-to-width-down/1000?cb=20240128012756',
        'INSANE': 'https://static.wikia.nocookie.net/geometry-dash/images/7/7f/Insane.png/revision/latest/scale-to-width-down/1000?cb=20240128012902',
        'EASY_DEMON': 'https://static.wikia.nocookie.net/geometry-dash/images/2/24/EasyDemon.png/revision/latest?cb=20240125115546',
        'MEDIUM_DEMON': 'https://static.wikia.nocookie.net/geometry-dash/images/e/e2/MediumDemon.png/revision/latest?cb=20240125115700',
        'HARD_DEMON': 'https://static.wikia.nocookie.net/geometry-dash/images/c/c4/Demon.png/revision/latest/scale-to-width-down/1000?cb=20240125115752',
        'INSANE_DEMON': 'https://static.wikia.nocookie.net/geometry-dash/images/1/11/InsaneDemon.png/revision/latest?cb=20240125115835',
        'EXTREME_DEMON': 'https://static.wikia.nocookie.net/geometry-dash/images/9/97/ExtremeDemon.png/revision/latest?cb=20240125115918',
        'UNRATED': 'https://static.wikia.nocookie.net/geometry-dash/images/6/68/Unrated.png/revision/latest/scale-to-width-down/1000?cb=20240128011828'
    }

    def __init__(self, difficulty):
        self.difficulty = difficulty

    def get_image(self) -> str:
        return self.DIFFICULTY_IMAGES.get(self.difficulty, self.DIFFICULTY_IMAGES['UNRATED'])