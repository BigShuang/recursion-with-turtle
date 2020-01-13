import turtle
size = 20
tower_width = 100
tower_height = 200
tower_radius = 10
tower_distance = 250
tower_altitude = -100

SPEED = 1


tower_loc = {
	"A": -1,
	"B": 0,
	"C": 1
}


tower_poles = {
	"A": [],
	"B": [],
	"C": []
}


FillColors=[
    "#d25b6a",
    "#d2835b",
    "#e5e234",
    "#83d05d",
    "#2862d2",
    "#35b1c0",
    "#5835c0"
]

def set_plate(i):
	l = size * (i+2)

	t = turtle.Turtle()
	t.hideturtle()
	t.penup()
	t.speed(0)

	t.left(90)
	t.begin_poly()
	t.forward(l)
	t.circle(size,180)
	t.forward(l * 2)
	t.circle(size,180)
	t.forward(l)
	t.end_poly()
	p = t.get_poly()

	turtle.register_shape("plate_%s" % i, p)


def set_tower():
	t = turtle.Turtle()
	t.hideturtle()
	t.penup()
	t.speed(0)

	t.left(90)
	t.begin_poly()
	t.forward(tower_width)
	t.circle(tower_radius,180)
	t.forward(tower_width-tower_radius)
	t.right(90)
	t.forward(tower_height)
	t.circle(tower_radius,180)
	t.forward(tower_height)
	t.right(90)
	t.forward(tower_width-tower_radius)
	t.circle(tower_radius,180)
	t.forward(tower_width)
	t.end_poly()
	p = t.get_poly()
	turtle.register_shape("tower",p)


def draw_towers():
	set_tower()
	tower = turtle.Turtle("tower")
	tower.speed(0)
	tower.penup()
	tower.goto(-tower_distance,tower_altitude)
	tower.stamp()
	tower.goto(0,tower_altitude)      
	tower.stamp()
	tower.goto(tower_distance,tower_altitude)

def draw_plates(pn):
	plates = []
	for i in range(pn):
		set_plate(i)
		_p = turtle.Turtle('plate_%s'%i)
		_p.penup()
		_p.speed(SPEED)
		_colorIdx = i % len(FillColors)
		_color = FillColors[_colorIdx]
		_p.color(_color, _color)
		plates.append(_p)

	return plates


def draw_move(plate, fromPole, toPole):
	to_x = tower_loc[toPole] * tower_distance
	toPole_count = len(tower_poles[toPole])
	to_y = tower_altitude + 2* tower_radius + toPole_count * size * 2

	if fromPole:
		tower_poles[fromPole].remove(plate)
		from_x = tower_loc[fromPole] * tower_distance
		plate.goto(from_x, tower_height)
		plate.goto(to_x, tower_height)

	plate.goto(to_x, to_y)
	tower_poles[toPole].append(plate)

def moveTower(height, fromPole, withPole, toPole, plates):
	if height == 1 :
		draw_move(plates[0], fromPole, toPole)
	else:
		moveTower(height-1, fromPole, toPole, withPole, plates)
		draw_move(plates[height-1], fromPole, toPole)
		moveTower(height-1, withPole, fromPole, toPole, plates)


if __name__ == '__main__':
	draw_towers()
	n = 5
	plates = draw_plates(n)

	for i in range(n):
		draw_move(plates[n-1 - i], '', 'A')

	moveTower(n, 'A', 'B', 'C', plates)

	turtle.done()