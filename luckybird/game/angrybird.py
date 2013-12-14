import physicalobject, resources

class AngryBird(physicalobject.PhysicalObject):
	
	def __init__(self, *args, **kwargs):
		super(AngryBird, self).__init__(*args,**kwargs)

	def handle_collision(self, another_object):
		if self.is_collide_with(another_object):
			self.death = True
			resources.collision_sound.play()
			return True
		else:
			return False
		
