import turtle
 
# ==============
#  常量设置
# ==============
N=7 # 汉诺塔层数限制
 
BasePL=12   # plate的大小基数，修改这个能够调整plate的大小
TowerP=5    # Tower的线宽
TowerW=110  # Tower的底座宽度
TowerH=200  # Tower的高度
TowerSpace=260  # Tower的之间的距离，从中心到中心
HORIZON=-100    # Tower的底座高度，用于定位
# 动画速度，5是比较适中的速度
PMS=0
 
# 优化处理
Isjump=True
 
POLES={
    "1": [],
    "2": [],
    "3": [],
}
PLATES=[] # 存储所有圆盘对象
 
# 塔的颜色
LineColor="black"
# 多个盘子的颜色
FillColors=[
    "#d25b6a",
    "#d2835b",
    "#e5e234",
    "#83d05d",
    "#2862d2",
    "#35b1c0",
    "#5835c0"
]
# 建立窗体
SCR=turtle.Screen()
# SCR.tracer()
SCR.setup(800,600) #设置窗体大小
 
 
# 设置圆盘形状
def set_plate(pi=0):
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
 
 
# 设置塔柱形状
def set_tower():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()
 
    t.begin_poly()
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
 
 
# 绘制塔柱
def draw_towers():
    set_tower()
    for tx in [-TowerSpace,0,TowerSpace]:
        t3 = turtle.Turtle('tower')
        t3.penup()
        t3.goto(tx,HORIZON)
 
 
# 绘制圆盘
def draw_plates(pn=4):
    plates=[]
    for i in range(pn):
        set_plate(i)
        _plate='plate_%s'%i
        _p=turtle.Turtle(_plate)
        _colorIdx = i % len(FillColors)
        _color=FillColors[_colorIdx]
 
        _p.color(_color,_color)
        _p.speed(PMS)
        plates.append(_p)
    # 反序，大的在前，小的在后
    global PLATES
    PLATES = plates[:]
 
# 绘制移动过程
def draw_move(diskIndex, fromPindex, toPindex):
    p=PLATES[diskIndex-1]
    index_loc={
        "A":1,
        "B":2,
        "C":3
    }
    toP=index_loc.get(toPindex,None)
    fromP=index_loc.get(fromPindex,None)
 
    p.penup()
 
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
 
 
# 将所有圆盘移动到起点
def movetoA(n,fromPindex):
    for i in range(n,0,-1):
        draw_move(i,None,fromPindex)
 
 
# 移动指定层圆盘diskIndex，从fromPole出发，到达toPole
def moveDisk(diskIndex,fromPole,toPole):
    """
    :param diskIndex: 圆盘的索引（从上往下，第一层为1，第二层为2、、、第n层为n）
    :param fromPole: 出发的柱子（起点）
    :param toPole: 要到达的柱子（终点）
    :return:
    """
    draw_move(diskIndex, fromPole, toPole)
 
 
# 核心函数，入口
def moveTower(height,fromPole, withPole, toPole):
    """
    :param height: 汉诺塔高度——层数
    :param fromPole: 出发的柱子（起点）
    :param withPole: 进过的柱子（中转点）
    :param toPole: 要到达的柱子（终点）
    :return:
    """
    if height == 1:
        # 基础情形：一层的汉诺塔
        moveDisk(1,fromPole, toPole)
        return
 
    # 先将圆盘1到n - 1看作一个整体从起点塔移动到中转塔（用目标塔作为本步骤的中转）
    moveTower(height-1,fromPole,toPole,withPole)
    # 再将圆盘n从起点塔A移动到目标塔C
    moveDisk(height,fromPole,toPole)
    # 最后将圆盘1到n - 1看作一个整体从中转塔移动到目标塔（用起点塔作为本步骤的中转）
    moveTower(height-1,withPole,fromPole,toPole)
 
 
if __name__ == '__main__':
    # 调用
    # 三层汉诺塔，A为出发柱子，B为中转柱子，C为目标柱子
    n=N
     
    SCR.tracer(0)
    draw_towers()
    draw_plates(n)
    movetoA(n,"A")
    SCR.tracer(1)
 
    # SCR.delay(3)
 
    moveTower(n,"A","B","C")
    turtle.done()