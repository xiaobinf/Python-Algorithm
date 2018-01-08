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
            if Y[i]*(sum(np.array(w)*np.array(X[i]))+b)<=0:
                w=np.array(w)+eta*Y[i]*np.array(X[i])
                b=b+Y[i]
                break
            if i==2:
                # 没有误分类点
                return w,b

def Gram(X):
    '''
    计算Gram矩阵G=[X[i]*X[j]]
    :param X:
    :return:
    '''
    n=len(X)
    G=np.matrix(np.zeros((n,n)))
    for i in range(len(X)):
        for j in range(len(X)):
            G[i,j]=sum(np.array(X[i])*np.array(X[j]))
    return G

def perception_dual(X,Y,eta=1,alpha=[0,0,0],b=0):
    '''
    感知机对偶形式
    :param X: 训练集数据X
    :param Y: 训练集标记Y
    :param eta: 梯度下降步长
    :return: w,b
    '''
    G=Gram(X)
    while True:
        for i in range(len(X)):
            # w*x+b<0为正确分类
            if Y[i] * (sum([alpha[j]*Y[j]*G[j,i] for j in range(len(X))])+b) <= 0:
                alpha[i] = alpha[i]+1
                b = b + Y[i]
                break
            if i == 2:
                # 没有误分类点
                w=sum([alpha[i]*Y[i]*np.array(X[i]) for i in range(len(X))])
                b=sum([alpha[i]*Y[i] for i in range(len(X))])
                print(alpha)
                return w, b



if __name__=="__main__":
    print(perception_origin(X,Y,eta=1,w=(0,0),b=0))
    print(Gram(X))
    print(perception_dual(X,Y,eta=1,alpha=[0,0,0],b=0))