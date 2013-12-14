import pyglet, math

def center_image(image):
	image.anchor_x = image.width/2
	image.anchor_y = image.height/2

def distance(point_1=(0,0),point_2=(0,0)):
	return math.sqrt((point_1[0]-point_2[0])**2 + (point_1[1]-point_2[1])**2)
