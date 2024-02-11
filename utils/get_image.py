def get_image(stars:int):
    if stars == 2:
        image = 'https://static.wikia.nocookie.net/geometry-dash/images/7/7a/Easy.png/revision/latest/scale-to-width-down/1000?cb=20240128012431'
    elif stars == 3:
        image = 'https://static.wikia.nocookie.net/geometry-dash/images/f/fb/Normal.png/revision/latest/scale-to-width-down/1000?cb=20231027082451'
    elif 4 <= stars <= 5:
        image = 'https://static.wikia.nocookie.net/geometry-dash/images/d/d5/Hard.png/revision/latest/scale-to-width-down/1000?cb=20240128012620'
    elif 6 <= stars <= 7:
        image = 'https://static.wikia.nocookie.net/geometry-dash/images/d/db/Harder.png/revision/latest/scale-to-width-down/1000?cb=20240128012756'
    else:
        image = 'https://static.wikia.nocookie.net/geometry-dash/images/7/7f/Insane.png/revision/latest/scale-to-width-down/1000?cb=20240128012902'
    return image
