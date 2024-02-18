
class Image:
    def __init__(self):
        pass

    def get_image(self,difficulty) -> str:
        difficulty = str(difficulty)[11:]
        if difficulty == 'AUTO':
            image = 'https://static.wikia.nocookie.net/geometry-dash/images/e/e8/Auto.png/revision/latest/scale-to-width-down/1000?cb=20240128012123'
        elif difficulty == 'EASY':
            image = 'https://static.wikia.nocookie.net/geometry-dash/images/7/7a/Easy.png/revision/latest/scale-to-width-down/1000?cb=20240128012431'
        elif difficulty == 'NORMAL':
            image = 'https://static.wikia.nocookie.net/geometry-dash/images/f/fb/Normal.png/revision/latest/scale-to-width-down/1000?cb=20231027082451'
        elif difficulty == 'HARD':
            image = 'https://static.wikia.nocookie.net/geometry-dash/images/d/d5/Hard.png/revision/latest/scale-to-width-down/1000?cb=20240128012620'
        elif difficulty == 'HARDER':
            image = 'https://static.wikia.nocookie.net/geometry-dash/images/d/db/Harder.png/revision/latest/scale-to-width-down/1000?cb=20240128012756'
        elif difficulty == 'INSANE':
            image = 'https://static.wikia.nocookie.net/geometry-dash/images/7/7f/Insane.png/revision/latest/scale-to-width-down/1000?cb=20240128012902'
        else:
            image = 'https://static.wikia.nocookie.net/geometry-dash/images/6/68/Unrated.png/revision/latest/scale-to-width-down/1000?cb=20240128011828'

        return image

    def get_demon_image(self,difficulty):
        difficulty = str(difficulty)[11:]
        if difficulty == 'EASY_DEMON':
            image = 'https://static.wikia.nocookie.net/geometry-dash/images/2/24/EasyDemon.png/revision/latest?cb=20240125115546'
        elif difficulty == 'MEDIUM_DEMON':
            image = 'https://static.wikia.nocookie.net/geometry-dash/images/e/e2/MediumDemon.png/revision/latest?cb=20240125115700'
        elif difficulty == 'HARD_DEMON':
            image = 'https://static.wikia.nocookie.net/geometry-dash/images/c/c4/Demon.png/revision/latest/scale-to-width-down/1000?cb=20240125115752'
        elif difficulty == 'INSANE_DEMON':
            image = 'https://static.wikia.nocookie.net/geometry-dash/images/1/11/InsaneDemon.png/revision/latest?cb=20240125115835'
        elif difficulty == 'EXTREME_DEMON':
            image = 'https://static.wikia.nocookie.net/geometry-dash/images/9/97/ExtremeDemon.png/revision/latest?cb=20240125115918'
        else:
            image = 'https://static.wikia.nocookie.net/geometry-dash/images/c/c4/Demon.png/revision/latest/scale-to-width-down/1000?cb=20240125115752'
        return image
