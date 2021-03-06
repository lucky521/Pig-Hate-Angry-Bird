import pyglet , random
import config, util, resources

conf = config.config()

class PhysicalObject(pyglet.sprite.Sprite):

	def __init__(self, *args, **kwargs):
		super(PhysicalObject, self).__init__(*args,**kwargs)
		# add two new value
		self.velocity_x = 0.0
		self.velocity_y = 0.0
		self.death = False
		
	def update(self, dt): #during time
		self.x += self.velocity_x * dt
		self.y += self.velocity_y * dt
		self.check_bounds()

	def check_bounds(self):
		min_x = -self.image.width/2
		min_y = -self.image.height/2
		max_x = conf.windows_width + self.image.width/2
		max_y = conf.windows_height + self.image.height/2
		if self.x < min_x:
			self.x = max_x
		elif self.x > max_x:
			self.x = min_x

		if self.y < min_y:
			self.y = max_y
		elif self.y > max_y:
			self.y = min_y
	
	def is_collide_with(self, another_object):
		collision_dis = self.image.width/2 + another_object.image.width/2;
		dis = util.distance(self.position, another_object.position)
		return (dis <= collision_dis)

	# one point is in object's internal?
	def is_internal(self, point=(0,0)):
		if util.abs_length(self.x, point[0]) > self.image.width/2:
			return False
		if util.abs_length(self.y, point[1]) > self.image.height/2:
			return False
		return True
		

