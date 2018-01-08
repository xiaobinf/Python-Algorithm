import numpy as np
import random

# 梯度下降算法 theta初始[1,1] m样本个数
# 用于做回归预测
def gradientDescent(x,y,theta,alpha,m,numIterations):
    '''
    用矩阵简化了计算  梯度下降算法结合了代数和矩阵两种方法 下午做
    :param x:
    :param y:
    :param theta:
    :param alpha:
    :param m:
    :param numIterations:
    :return:
    '''
    print(np.shape(x))
    print(np.shape(theta))
    xTrans=x.transpose()
    for i in range(numIterations):
        hypothesis=np.dot(x,theta)
        loss=hypothesis-y
        # loss 是 np的array 可以用于array**2
        cost=np.sum(loss**2)/(m*2)
        print("Iteration %d | Cost: %f" % (i, cost))
        gradient = np.dot(xTrans, loss) / m
        theta = theta - alpha * gradient
    return theta


def gradientDescent_1(x,y,theta,alpha,m,numIterations):
    '''
    用矩阵简化了计算  梯度下降算法结合了代数和矩阵两种方法 下午做
    :param x:
    :param y:
    :param theta:
    :param alpha:
    :param m:
    :param numIterations:
    :return:
    '''
    pass

def genData(numPoints,bias,variance):
    '''

    :param numPoints: 生成测试数据的个数
    :param bias: 偏量
    :param variance:方差
    :return: x矩阵 y向量
    '''
    x=np.zeros(shape=(numPoints,2))
    y=np.zeros(shape=(numPoints))
    for i in range(numPoints):
        x[i][0],x[i][1]=1,i
        y[i]=i+bias+random.uniform(0,1)*variance
    return x,y


def test():
    x, y = genData(100, 25, 10)
    print(x, y)
    numIterations = 100000
    # alpha 人工定义
    alpha = 0.0005
    m, n = np.shape(x)
    # shape(theta) n *, n=2
    theta = np.ones(n)
    # print(theta)
    # print("theta shape",np.shape(theta))
    theta = gradientDescent(x, y, theta, alpha, m, numIterations)
    print(theta)

from sklearn import linear_model
def test_1():
    x, y = genData(100, 25, 10)
    regr=linear_model.LinearRegression()
    regr.fit(x,y)
    print(regr.coef_,regr.intercept_)

if __name__=='__main__':
    test()
    test_1()

