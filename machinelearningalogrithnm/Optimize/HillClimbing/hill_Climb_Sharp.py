# encoding:utf8
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


def drawPaht(X, Y, Z, px, py, pz):
    fig = plt.figure()
    ax = Axes3D(fig)
    plt.title("demo_hill_climbing")
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow', )
    ax.set_xlabel('x label', color='r')
    ax.set_ylabel('y label', color='g')
    ax.set_zlabel('z label', color='b')
    ax.plot(px, py, pz, 'r.')  # 绘点
    plt.show()


def hill_climb(X, Y):
    global_X = []
    global_Y = []

    len_x = len(X)
    len_y = len(Y)
    # 随机登山点
    st_x = randint(0, len_x - 1)
    st_y = randint(0, len_y - 1)

    def argmax(stx, sty, nextx, nexty):
        '''
        返回当前点和周围点中函数值较高的点的坐标
        :param stx: 当前点横坐标
        :param sty: 当前点纵坐标
        :param nextx: 下一个点的横坐标
        :param nexty:下一个点的纵坐标
        :return: 当前点和周围点中函数值较高的点的坐标
        '''
        cur = func(X[0][stx], Y[sty][0])
        next = func(X[0][nextx], Y[nexty][0])
        if cur < next:
            return nextx, nexty
        return stx, sty
        #return cur < next and alisx, alisy or stx, sty

    tmp_x = st_x
    tmp_y = st_y
    while (len_x > st_x >= 0) or (len_y > st_y >= 0):
        # 比较四个点的高度 求出最高的点
        if st_x + 1 < len_x:
            tmp_x, tmp_y = argmax(tmp_x, tmp_y, (st_x + 1), st_y)

        if st_x >= 1:
            tmp_x, tmp_y = argmax(tmp_x, tmp_y, st_x - 1, st_y)

        if st_y + 1 < len_x:
            tmp_x, tmp_y = argmax(tmp_x, tmp_y, st_x, st_y + 1)

        if st_y >= 1:
            tmp_x, tmp_y = argmax(tmp_x, tmp_y, st_x, st_y - 1)

        if tmp_x != st_x or tmp_y != st_y:
            st_x = tmp_x
            st_y = tmp_y
        else:
            break
        global_X.append(X[0][st_x])
        global_Y.append(Y[st_y][0])
    return global_X, global_Y, func(X[0][st_x], Y[st_y][0])


if __name__ == '__main__':
    X = np.arange(-2, 4, 0.1)
    Y = np.arange(-2, 4, 0.1)
    X, Y = np.meshgrid(X, Y)
    Z = func(X, Y, 1.7, 1.7)
    px, py, maxhill = hill_climb(X, Y)
    print(px, py, maxhill)
    drawPaht(X, Y, Z, px, py, func(np.array(px), np.array(py), 1.7, 1.7))