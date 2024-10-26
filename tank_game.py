import pgzrun

WIDTH = 800
HEIGHT = 600

tank = Actor('tank_red')
tank.y = 575
tank.x = 400
tank.angle = 90

background =  Actor('grass')

walls = []
for x in range(16):
	for y in range(12):
		wall = Actor('wall')
		wall.x = x * 50
		wall.y = y * 50

def update():
	if keyboard.left:
		tank.x = tank.x - 2
		tank.angle = 180
	elif keyboard.right:
		tank.x = tank.x + 2
		tank.angle = 0
	elif keyboard.up:
		tank.y = tank.y - 2
		tank.angle = 90
	elif keyboard.down:
		tank.y = tank.y + 2
		tank.angle = 270

def draw():
    screen.fill((0,0,0))
    background.draw()
    tank.draw()
    for wall in walls:
    	wall.draw()

pgzrun.go()