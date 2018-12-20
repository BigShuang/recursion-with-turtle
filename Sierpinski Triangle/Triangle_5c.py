# 谢尔宾斯基三角形
# By BigShuang
import math
import turtle

# 颜色
LineColor="black"
FillColors=[
    '#CAE1FF',
    '#FFEFDB',
    '#8470FF',
    '#FF6347',
    '#FFDEAD',
    '#C1FFC1'
]


# 最小绘制长度-三角形最小边长
Base=10
# 三角形边长
TriSize=250
# 绘制速度
MPS=10

# 初始化Turtle对象
t = turtle.Turtle()
t.speed(MPS)
# t.screen.delay(0)
t.hideturtle()


# 递归函数-画下一级别的三角形-内部更小的
def draw_nextone(*triangle,**kwargs):
    # 如果三角形边长大于最小绘制长度,退出递归
    if get_edge(triangle)<Base:
        return
    # 否则
    # 1-根据三边中点绘制内部三角形
    a, b, c = triangle[0:3]
    a_b, a_c, b_c=get3mid(a, b, c)
    # 绘制三角形并填色
    depth=kwargs.get("depth",0)
    if len(triangle)==4:
        depth=triangle[3]

    # 取对应深度的颜色
    _colorIdx=depth%len(FillColors)
    # if depth<
    color = FillColors[_colorIdx]
    # if depth<len(FillColors):
    #
    #     color=FillColors[depth]
    draw_tri(a_b, a_c, b_c, color=color)
    # 2-得到三个更小的三角形，对这三个更小的三角形再次调用本函数
    draw_nextone(a,a_b,a_c,depth=depth+1)
    draw_nextone(b, a_b, b_c,depth=depth+1)
    draw_nextone(c, a_c, b_c,depth=depth+1)


# 得到三角行三边边长
def get_edge(triangle):
    # triangle:[(),(),()]-三点坐标组成的列表
    a,b,c=triangle[0:3]
    ax,ay=a
    bx,by=b
    ab2=(ax-bx)**2+(ay-by)**2
    return math.sqrt(ab2)


# 得到三边中点
def get3mid(*triangle):
    # triangle:[(),(),()]-三点坐标组成的列表
    a, b, c = triangle
    ax, ay = a
    bx, by = b
    cx, cy=c
    # 得到三边中点的坐标
    a_b=((ax+bx)/2,(ay+by)/2)
    a_c = ((ax + cx) / 2, (ay + cy) / 2)
    b_c = ((cx + bx) / 2, (cy + by) / 2)
    return a_b,a_c,b_c


# 根据顶点坐标绘制三角形，可选颜色
def draw_tri(*args,**kwargs):
    # 三点坐标
    a, b, c =args
    # 填充颜色
    color=kwargs.get('color',None)

    t.penup()
    t.setpos(a)
    if color:
        t.color(LineColor,color)
        t.begin_fill()
    t.pendown()
    t.goto(b)
    t.goto(c)
    t.goto(a)
    t.penup()
    if color:
        t.end_fill()


if __name__ == '__main__':
    _edge=TriSize*math.sqrt(3)
    tri=[(-TriSize,-TriSize),(TriSize,-TriSize),(0,_edge-TriSize)]
    a,b,c=tri
    draw_tri(a,b,c)
    draw_nextone(a,b,c)
    turtle.done()
