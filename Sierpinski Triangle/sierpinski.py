#!/usr/bin/python3
import turtle


t = turtle.Turtle()


def get_midpoint(a, b):
    ax, ay = a
    bx, by = b
    return (ax + bx) / 2, (ay + by) / 2


def draw_triangle(a, b, c):
    ax, ay = a
    bx, by = b
    cx, cy = c

    t.penup()
    t.goto(ax, ay)
    t.pendown()
    t.goto(bx, by)
    t.goto(cx, cy)
    t.goto(ax, ay)
    t.penup()


def draw_sierpinski(triangle, depth):
    a, b, c = triangle
    draw_triangle(a, b, c)
    if depth == 0:
        return
    else:
        d = get_midpoint(a, b)
        e = get_midpoint(b, c)
        f = get_midpoint(c, a)
        draw_sierpinski([a, d, f], depth-1)
        draw_sierpinski([d, b, e], depth-1)
        draw_sierpinski([f, e, c], depth-1)


if __name__ == '__main__':
    triangle = [[-200, -100], [0, 200], [200, -100]]
    draw_sierpinski(triangle, 2)
    turtle.done()
