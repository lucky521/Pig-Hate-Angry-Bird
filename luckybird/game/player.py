import physicalobject, resources
from pyglet.window import key
import config

global conf
conf = config.config()

class Player(physicalobject.PhysicalObject):
	
	def __init__(self, *args, **kwargs):
		super(Player, self).__init__(img=resources.player_image,
						*args,**kwargs)

		self.accelerate = conf.player_speed
		self.key_handler = key.KeyStateHandler()
	

	def on_key_press(self, symbol, modifiers):
		if symbol == key.SPACE:
			self.accelerate = 3 * conf.player_speed
	
	def on_key_release(self, symbol, modifiers):
		if symbol == key.SPACE:
			self.accelerate = conf.player_speed
	
	def update(self, dt):
		super(Player, self).update(dt)
			
		if self.key_handler[key.LEFT]:
			self.x -= self.accelerate
		if self.key_handler[key.RIGHT]:
			self.x += self.accelerate
		if self.key_handler[key.UP]:
			self.y += self.accelerate
		if self.key_handler[key.DOWN]:
			self.y -= self.accelerate
	
	def delete(self):
		super(Player, self).delete()
