import pyglet
from util import center_image

# Tell pyglet where to find the resources
pyglet.resource.path = ['../resources']
pyglet.resource.reindex()


player_image = pyglet.resource.image("pig80.png")
center_image(player_image)

egg_image = pyglet.resource.image("egg80.png")
center_image(egg_image)


red_bird_image1 = pyglet.resource.image("red180.png")
center_image(red_bird_image1)

red_bird_image2 = pyglet.resource.image("red280.png")
center_image(red_bird_image2)

red_bird_image3 = pyglet.resource.image("red380.png")
center_image(red_bird_image3)

white_bird_image = pyglet.resource.image("white80.png")
center_image(white_bird_image)

yellow_bird_image = pyglet.resource.image("yellow80.png")
center_image(yellow_bird_image)

black_bird_image = pyglet.resource.image("black80.png")
center_image(black_bird_image)


getegg_sound = pyglet.resource.media("getegg.wav", streaming=False)

collision_sound = pyglet.resource.media("collision.wav", streaming=False)
