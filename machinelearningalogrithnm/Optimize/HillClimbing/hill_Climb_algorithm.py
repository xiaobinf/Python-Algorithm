from random import random, randint

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def func(X, Y, x_move=1.7, y_move=1.7):
    def mul(X, Y, alis=1):
        return alis * np.exp(-(X * X + Y * Y))

    return mul(X, Y) + mul(X - x_move, Y - y_move, 2)


def show(X, Y, Z):
    fig = plt.figure()
    ax = Axes3D(fig)
    plt.title("demo_hill_climbing")
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow', )
    ax.set_xlabel('x label', color='r')
    ax.set_ylabel('y label', color='g')
    ax.set_zlabel('z label', color='b')
    # ax.scatter(X,Y,Z,c='r') #绘点
    plt.show()


def drawPaht(X, Y, Z,px,py,pz):
    fig = plt.figure()
    ax = Axes3D(fig)
    plt.title("demo_hill_climbing")
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow', )
    ax.set_xlabel('x label', color='r')
    ax.set_ylabel('y label', color='g')
    ax.set_zlabel('z label', color='b')
    ax.plot(px,py,pz,'r.') #绘点
    plt.show()


def hill_climb(X, Y):
    global_X = []
    global_Y = []

    len_x = len(X)
    len_y = len(Y)
    # 随机登山点
    st_x = randint(0, len_x-1)
    st_y = randint(0, len_y-1)

    def argmax(stx, sty, alisx=0, alisy=0):
        cur = func(X[0][st_x], Y[st_y][0])
        next = func(X[0][st_x + alisx], Y[st_y + alisy][0])

        return cur < next and True or False

    while (len_x > st_x >= 0) or (len_y > st_y >= 0):
        # 在二维平面网格上 点(x,y)上下左右移动判断各一次
        if st_x + 1 < len_x and argmax(st_x, st_y, 1):
            st_x += 1
        elif st_y + 1 < len_x and argmax(st_x, st_y, 0, 1):
            st_y += 1
        elif st_x >= 1 and argmax(st_x, st_y, -1):
            st_x -= 1
        elif st_y >= 1 and argmax(st_x, st_y, 0, -1):
            st_y -= 1
        else:
            break
        # (global_X,global_Y)表示不断更新的全局最优点 爬山的点
        global_X.append(X[0][st_x])
        global_Y.append(Y[st_y][0])
    return global_X, global_Y, func(X[0][st_x], Y[st_y][0])


if __name__ == '__main__':
    X = np.arange(-2, 4, 0.1)
    Y = np.arange(-2, 4, 0.1)
    X, Y = np.meshgrid(X, Y)
    print(X,Y)
    Z = func(X, Y, 1.7, 1.7)
    px, py, maxhill = hill_climb(X, Y)
    print('px:',px)
    print('py:',py)
    print('maxhill:',maxhill)
    drawPaht(X, Y, Z,px,py,func(np.array(px), np.array(py), 1.7, 1.7))