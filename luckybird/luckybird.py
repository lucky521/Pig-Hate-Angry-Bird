import pyglet, time
from game import resources, load, player, config

start_time = time.time()
isdead = False
get_egg_num = 0

conf = config.config()
mywin = pyglet.window.Window(conf.windows_width, conf.windows_height)
pyglet.gl.glClearColor(0,0,0,0.9)


main_batch = pyglet.graphics.Batch()

score_label = pyglet.text.Label(text="Time: 0", bold=True, x=2, y=5, batch=main_batch)
egg_num_label = pyglet.text.Label(text="Egg: 0", bold=True, x=100, y=5, batch=main_batch)
level_label = pyglet.text.Label(text="Lucky Bird",bold=True,
				x=conf.windows_width/2,
				y=conf.windows_height-20,
				anchor_x='center', batch=main_batch)

player_ship = player.Player(x=conf.windows_width/2,
				y=conf.windows_height/2,
				batch=main_batch)

angrybirds = load.angrybirds(conf.bird_num, player_ship.position, main_batch)
eggs = load.eggs(1, player_ship.position, main_batch)
player_lives = load.player_lives(conf.player_life_num, main_batch)


mywin.push_handlers(player_ship.key_handler)
mywin.push_handlers(player_ship)


@mywin.event
def on_draw():
	mywin.clear()
	main_batch.draw()


def update(dt):
	global isdead, angrybirds, eggs, get_egg_num
	if isdead:
		return
	score_label.text = "Time: " + str(int(time.time() - start_time))

	newbirdlist = []
	for bird in angrybirds:
		if bird.handle_collision(player_ship):
			bird.delete()
			player_lives.pop()
			if len(player_lives) == 0:
				player_ship.delete()
				gameover_label = pyglet.text.Label(text="Game Over", 
									font_size=30.0,
									bold=True, 
									x=conf.windows_width/2, 
									y=conf.windows_height/2, 
									anchor_x='center',
									batch=main_batch)
				isdead = True
				return
		else:
			newbirdlist.append(bird)


	angrybirds = newbirdlist

	newegglist = []
	for egg in eggs:
		if egg.handle_collision(player_ship):
			egg.delete()
			get_egg_num += 1
			egg_num_label.text = "Egg: " + str(get_egg_num) 
		else:
			newegglist.append(egg)
	eggs = newegglist


	for obj in angrybirds:
		obj.update(dt)
	for obj in eggs:
		obj.update(dt)
	player_ship.update(dt)
	


def add_bird(dt):
	global angrybirds
	new_bird = load.angrybirds(1, player_ship.position, main_batch)
	angrybirds += new_bird

def add_egg(dt):
	global eggs
	new_egg = load.eggs(1, player_ship.position, main_batch)
	eggs += new_egg



if __name__ == "__main__":
	#resources.bk_sound.play()
	pyglet.clock.schedule_interval(update, conf.dt)
	pyglet.clock.schedule_interval(add_bird, conf.addbird_time)
	pyglet.clock.schedule_interval(add_egg, conf.addegg_time)
	pyglet.app.run()
