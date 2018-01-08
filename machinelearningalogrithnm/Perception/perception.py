import os
import sys
import numpy as np

# An example in that book, the training set and parameters' sizes are fixed
training_set = []

w = []
b = 0
lens = 0
n = 0

X=[(3,3),(4,3),(1,1)]
Y=[1,1,-1]

def perception_origin(X,Y,eta=1,w=(0,0),b=0):
    '''
    感知机原始形式  f(x)=sign(w*x+b)
    :param X: 训练集数据X
    :param Y: 训练集标记Y
    :param eta: 梯度下降步长
    :return: w,b
    '''
    while True:
        for i in range(len(X)):
            # w*x+b<0为正确分类
            print(i)
            print(np.array(w),np.array(X[i]))
            print(Y[i]*(sum(np.array(w)*np.array(X[i]))+b))
            if Y[i]*(sum(np.array(w)*np.array(X[i]))+b)<=0:
                print(Y[i])
                w=np.array(w)+eta*Y[i]*np.array(X[i])
                b=b+Y[i]
                break
            if i==2:
                # 没有误分类点
                return w,b


if __name__=="__main__":
    print(perception_origin(X,Y,eta=1,w=(0,0),b=0))
