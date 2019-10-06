# coding:utf-8
# 迷宫探索
# By BigShuang
import turtle
import random

# ========================
# 常量
# ========================
# 设置用于绘制迷宫的单元格的尺寸
CELL_SIZE = 20
# 设置打点(起点和终点)的尺寸
DOT_SIZE = 15
# 设置探索过程（也就是路径）的尺寸
LINE_SIZE = 5
TXT_PATH = "text/301.txt"

# ========================
# 初始化一些turtle画笔对象
# ========================
scr = turtle.Screen()  # 建立屏幕对象 src
scr.colormode(255)  # 设置颜色模式为rgb数值模式

wall_t = turtle.Turtle()  # 建立画笔对象 wall_t 用于绘制墙体
dot_t = turtle.Turtle()  # 建立画笔对象 dot_t 用于绘制点
line_t = turtle.Turtle()  # 建立画笔对象 line_t 用于绘制探索过程（也就是路径）
line_t.pensize(LINE_SIZE)


# 从txt文本中将迷宫提取出来
def get_maze_info(filename):
    with open(filename, 'r') as f:
        fl = f.readlines()

    maze_list = []
    for line in fl:
        line = line.strip()
        line_list = line.split(" ")
        maze_list.append(line_list)

    return maze_list


mazeList = get_maze_info(TXT_PATH)
# 获取迷宫的长宽，R-行数，C-列数
R, C = len(mazeList), len(mazeList[0])
scr.setup(width=C * CELL_SIZE, height=R * CELL_SIZE)  # 设置屏幕尺寸大小（刚好能够显示所有迷宫的单元格）


def draw_cell(ci, ri):
    """
    绘制一个墙体单元格,
    :param ci: 单元格所在列序号
    :param ri: 单元格所在行序号
    :return:
    """
    # 计算出单元格左上角的坐标，计算演示图在本段代码下方
    tx = ci * CELL_SIZE - C * CELL_SIZE / 2
    ty = R * CELL_SIZE / 2 - ri * CELL_SIZE
    wall_t.penup()  # 提起画笔
    wall_t.goto(tx, ty)  # 根据计算出来的坐标移动到单元格左上角

    # 为了美化样式，我们需要把黑色弄的有变化些，即有不同的灰度
    v = random.randint(100, 150)
    wall_t.color(v, v, v)

    wall_t.pendown()  # 放下画笔
    wall_t.begin_fill()  # 开启填充，此时经过的形状会被填充
    # 绘制一个边长为CELL_SIZE的正方形
    for i in range(4):
        wall_t.fd(CELL_SIZE)
        wall_t.right(90)
    wall_t.end_fill()  # 关闭填充


def draw_dot(ci, ri, color="black"):
    """
        在制定单元格绘制圆点,
        :param ci: 单元格所在列序号
        :param ri: 单元格所在行序号
        :param color: 圆点的颜色
        :return:
    """
    # 计算出单元格左上角的坐标，计算演示图在本段代码下方
    tx = ci * CELL_SIZE - C * CELL_SIZE / 2
    ty = R * CELL_SIZE / 2 - ri * CELL_SIZE
    # 进一步计算出所在单元格中心的坐标
    cx = tx + CELL_SIZE / 2
    cy = ty - CELL_SIZE / 2
    dot_t.penup()

    dot_t.goto(cx, cy)
    dot_t.dot(DOT_SIZE, color)


# 根据迷宫信息绘制迷宫
def draw_maze(mazeList):
    scr.tracer(0)  # 具体我也没搞明白，只知道能够跳过漫长的绘制动画

    # 　rowIndex，行号，相当于ｙ
    for rowIndex in range(len(mazeList)):
        row = mazeList[rowIndex]
        for columnIndex in range(len(row)):
            # columnIndex，列号，相当于ｘ
            item = row[columnIndex]
            if item == "1" or item == "2":
                draw_cell(columnIndex, rowIndex)  # 绘制具体的单元格
            elif item == "S":
                # 设置起点颜色为蓝色
                draw_dot(columnIndex, rowIndex, "blue")
            elif item == "E":
                # 设置终点颜色为绿色
                draw_dot(columnIndex, rowIndex, "green")


# 绘制路径，以画笔当前所在位置为起点，以单元格（ci, ri）中心作为终点，绘制路径。
def draw_path(ci, ri, color="blue"):
    # 计算出单元格左上角的坐标，计算演示图在本段代码下方
    tx = ci * CELL_SIZE - C * CELL_SIZE / 2
    ty = R * CELL_SIZE / 2 - ri * CELL_SIZE
    # 进一步计算出所在单元格中心的坐标
    cx = tx + CELL_SIZE / 2
    cy = ty - CELL_SIZE / 2

    line_t.color(color)
    line_t.goto(cx, cy)


# 核心递归探索方法，从该点出发，递归地去探索四个方向
def searchNext(mazeList, ci, ri):
    # 1,找到终点，探索完成，然后告诉上一步这一步探索成功
    if mazeList[ri][ci] == "E":
        draw_path(ci, ri)
        return True

    # 2,找到墙或者探索过的点（或者超出迷宫的点），探索失败，然后还是告诉上一步这一步探索是失败的
    if not (0 <= ci < len(mazeList[0]) and 0 <= ri < len(mazeList)):
        return False
    if mazeList[ri][ci] in ["1", "2", "TRIED"]:
        return False

    # 探索后标记该点为已探索过
    mazeList[ri][ci] = "TRIED"
    draw_path(ci, ri)

    # 上下左右四个探索的方向
    direction = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1],
    ]

    for d in direction:
        dc, dr = d

        found = searchNext(mazeList, ci + dc, ri + dr)
        if found:
            # 3,向某个方向的探索得出的结论是成功的（源于1），那么探索完成，不在探索，并且告诉上一步探索这一方向是能够探索成功的
            draw_path(ci, ri, "green")
            return True
        else:
            # 4,向某个方向的探索得出的结论是失败的（源于2），那么换一个方向进行探索
            draw_path(ci, ri, "red")

    # 5,向所有方向探索都失败了，那么探索失败，并告诉上一步这一方向探索是失败的
    return False


# 　开始迷宫探索
def start_search(mazeList):
    # 获取起点所在行和列的序号
    start_c, start_r = 0, 0
    # 　rowIndex，行号，相当于ｙ
    for rowIndex in range(len(mazeList)):
        row = mazeList[rowIndex]
        for columnIndex in range(len(row)):
            # columnIndex，列号，相当于ｘ
            item = row[columnIndex]
            if item == "S":
                start_c, start_r = columnIndex, rowIndex

    line_t.penup()
    draw_path(start_c, start_r)
    line_t.pendown()
    # 进入递归搜索
    searchNext(mazeList, start_c, start_r)


draw_maze(mazeList)
scr.tracer(1)
start_search(mazeList)
# 绘制玩的话会发现窗口会自动退出掉，加入下面一行代码就可以维持住窗口
turtle.done()