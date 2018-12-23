#! /usr/bin/python
# -*- coding:utf-8 -*-
import turtle
import time

# ==============
#  常量设置
# ==============
PILENUM=7

BasePL=12   # plate的大小基数，修改这个能够调整plate的大小
TowerP=5    # Tower的线宽
TowerW=110  
TowerH=200
TowerSpace=260
HORIZON=-100
# 5是比较适中的速度
PMS=8

# 优化处理
Isjump=True

POLES={
    "1": [],
    "2": [],
    "3": [],
}

LineColor="black"
FillColors=[
    "#d25b6a",
    "#d2835b",
    "#e5e234",
    "#83d05d",
    "#2862d2",
    "#35b1c0",
    "#5835c0"
]

SCR=turtle.Screen()
# SCR.tracer()
SCR.delay(1)
SCR.setup(800,600)

def init_plate(pi=0):
    _pi=pi+2
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
    t.begin_poly()
    t.left(90)
    t.forward(BasePL*_pi)
    t.circle(BasePL, 180)
    t.forward(BasePL * 2 * _pi)
    t.circle(BasePL, 180)
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

# P格式说明
def moveTower(Plates,fromP,toP,midP):
    # Plates 大的在前，小的在后
    if len(Plates)>1:
        # Move a tower of height-1 to an intermediate pole, using the final pole.
        moveTower(Plates[1:], fromP, midP, toP)
        # Move the remaining disk to the final pole.
        moveDisk(Plates[0],fromP, toP)
        # Move the tower of height-1 from the intermediate pole to the final pole using the original pole.
        moveTower(Plates[1:], midP, toP, fromP)
    else:
        moveDisk(Plates, fromP, toP)


def moveDisk(Plates, fromP, toP):
    if not (isinstance(Plates,list) or isinstance(Plates,tuple)):
        Plates=[Plates]

    for p in Plates:
        p.penup()
        # p.speed()

        mx = (toP - 2) * TowerSpace
        my = HORIZON + len(POLES[str(toP)]) * BasePL * 2

        if fromP!=None:
            POLES[str(fromP)].remove(p)
            if Isjump:
                px,py=p.pos()
                p.goto(px,TowerH+py)
                p.goto(mx,TowerH+py)

        p.goto(mx, my)
        POLES[str(toP)].append(p)

def get_plates(pn=4):
    plates=[]
    for i in range(pn):
        init_plate(i)
        _plate='plate_%s'%i
        _p=turtle.Turtle(_plate)
        _colorIdx = i % len(FillColors)
        _color=FillColors[_colorIdx]

        _p.color(_color,_color)
        _p.speed(PMS)
        plates.append(_p)
    # 反序，大的在前，小的在后
    return plates[::-1]


def show_towers():
    init_tower()
    for tx in [-TowerSpace,0,TowerSpace]:
        t3 = turtle.Turtle('tower')
        t3.penup()
        t3.goto(tx,HORIZON)


def main(*args):
    show_towers()
    plates = get_plates(PILENUM)
    moveDisk(plates, None, 1)
    moveTower(plates, 1, 3, 2)
    # turtle.done()

def test1():
    init_plate(2)
    _plate = 'plate_%s' % 2
    p = turtle.Turtle(_plate)
    c=FillColors[2]
    p.color("black", c)
    for i in range(8):
        p.forward(200)
        p.left(90)

if __name__ == '__main__':
    # main()
    SCR.onclick(main)
    # test1()
    turtle.done()

    pass
