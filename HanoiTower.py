#! /usr/bin/python
# -*- coding:utf-8 -*-
import turtle


BasePL=10
TowerP=5
TowerW=100
TowerH=300
TowerSpace=300
HORIZON=-100


SCR=turtle.Screen()
SCR.tracer()


def init_plate(pi=0):
    _pi=pi+2
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.begin_poly()
    t.left(90)
    t.forward(BasePL*_pi)
    t.circle(10, 180)
    t.forward(BasePL * 2 * _pi)
    t.circle(10, 180)
    t.forward(BasePL * _pi)
    t.end_poly()
    p = t.get_poly()
    pname='plate_%s'%pi
    SCR.register_shape(pname, p)


def init_tower():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()

    t.begin_poly()
    # t.pensize(TowerP)
    t.left(90)
    t.forward(TowerW)
    t.circle(-TowerP, 180)
    t.forward(TowerW)
    t.forward(TowerW)
    t.circle(-TowerP, 180)
    t.forward(TowerW-TowerP/2)

    t.left(90)
    t.forward(TowerH)
    t.circle(-TowerP, 180)
    t.forward(TowerH)
    t.end_poly()
    p = t.get_poly()
    SCR.register_shape('tower', p)





def moveTower(height,fromP,toP,midP):
    if height>1:
        # Move a tower of height-1 to an intermediate pole, using the final pole.
        moveTower(height - 1, fromP, midP, toP)
        # Move the remaining disk to the final pole.
        moveDisk(height,fromP, toP)
        # Move the tower of height-1 from the intermediate pole to the final pole using the original pole.
        moveTower(height - 1, midP, toP, fromP)
    else:
        moveDisk(height, fromP, toP)


def moveDisk(height, fromP, toP):
    pass


def get_plates(pn=4):
    plates=[]
    for i in range(pn):
        init_plate(i)
        _plate='plate_%s'%i
        plates.append(turtle.Turtle(_plate))
    return plates


def show_towers():
    init_tower()
    for tx in [-TowerSpace,0,TowerSpace]:
        t3 = turtle.Turtle('tower')
        t3.penup()
        t3.goto(tx,HORIZON)
        print t3.pos()


if __name__ == '__main__':
    show_towers()
    plates=get_plates(4)

    turtle.done()


