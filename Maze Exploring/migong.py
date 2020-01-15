import turtle
import random

def get_maze_info(filename):
	with open(filename, 'r') as f:
		fl = f.readlines()

	maze_list = []
	for line in fl:
		line = line.strip()
		line_list = line.split(" ")
		maze_list.append(line_list)

	return maze_list


txt_path = "text/301.txt"
mazeList = get_maze_info(txt_path)
# print(mazeList)

R, C = len(mazeList), len(mazeList[0])
cellsize = 20
dot_size = 15
dot_t = turtle.Turtle()
line_t = turtle.Turtle()
line_t.pensize(5)
line_t.speed(0)


scr = turtle.Screen()
scr.setup(width=C*cellsize, height=R*cellsize)
scr.colormode(255)

t=turtle.Turtle()
t.speed(0)


def draw_cell(ci, ri):
	tx = ci*cellsize - C*cellsize/2
	ty = R*cellsize/2 - ri*cellsize

	t.penup()
	t.goto(tx, ty)

	v = random.randint(100, 150)
	t.color(v, v, v)

	t.pendown()
	t.begin_fill()
	for i in range(4):
		t.fd(cellsize)
		t.right(90)
	t.end_fill()

def draw_dot(ci, ri, color):
	tx = ci*cellsize - C*cellsize/2
	ty = R*cellsize/2 - ri*cellsize

	cx = tx+cellsize/2
	cy = ty-cellsize/2
	dot_t.penup()
	dot_t.goto(cx,cy)
	dot_t.dot(dot_size,color)


def draw_maze(maze_list):
	scr.tracer(0)

	for ri in range(R):
		for ci in range(C):
			item = maze_list[ri][ci]
			if item in ['1', '2']:
				draw_cell(ci, ri)
			elif item == "S":
				draw_dot(ci,ri, "blue")
			elif item == "E":
				draw_dot(ci, ri, "green")


def draw_path(ci,ri, color="blue"):
	tx = ci*cellsize - C*cellsize/2
	ty = R*cellsize/2 - ri*cellsize

	cx = tx+cellsize/2
	cy = ty-cellsize/2

	line_t.color(color)
	line_t.goto(cx, cy)


def searchNext(mazeList, ci, ri):
	if mazeList[ri][ci] == "E":
		draw_path(ci, ri)
		return True

	if not (0<=ci<C and 0<=ri<R):
		return False
	if mazeList[ri][ci] in ['1','2', 'TRIED']:
		return False

	mazeList[ri][ci] = "TRIED"
	draw_path(ci, ri)

	direction = [
		(1, 0),
		(-1,0),
		(0, 1),
		(0, -1)
	]

	for d in direction:
		dc, dr = d

		found = searchNext(mazeList, ci + dc, ri +dr)
		if found:
			draw_path(ci, ri, "green")
			return True
		else:
			draw_path(ci, ri, "red")

	return False


def start_search(mazeList):
	start_r, start_c = 0, 0
	for ri in range(R):
		for ci in range(C):
			item = mazeList[ri][ci]
			if item == "S":
				start_r, start_c = ri, ci

	line_t.penup()
	draw_path(start_c, start_r)
	line_t.pendown()
	searchNext(mazeList,start_c, start_r)


draw_maze(mazeList)
scr.tracer(1)
start_search(mazeList)
turtle.done()