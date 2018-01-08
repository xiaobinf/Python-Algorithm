import numpy as np
import math

# X,Y线性回归的计算方法
# 1.简单线性回归计算方法  machinelearningalogrithnm/Regression/LinearRegression/SimpleLinearRegression.py
# 2.z1=numpy.polyfit(X,Y,degree=1) 返回 多项式参数
# p=numpy.poly1d(z1)     p(x)可以作为拟合曲线的函数

#皮尔逊相关系数
def computeCorrelation(X,Y):
    x_bar=np.mean(X)
    y_bar=np.mean(Y)
    SSR=0
    VarX=0
    VarY=0
    for i in range(len(X)):
        diffXX_bar=X[i]-x_bar
        diffYY_bar=Y[i]-y_bar
        SSR+=diffXX_bar*diffYY_bar
        VarX+=diffXX_bar**2
        VarY+=diffYY_bar**2
    r=SSR/math.sqrt(VarX*VarY)
    return r

#计算R平方值
def polyfit(x,y,degree):
    results={}
    coeffs=np.polyfit(x,y,degree)
    print('coeffs:',coeffs)
    results['polynomical']=coeffs.tolist()
    p=np.poly1d(coeffs)
    print('p:',p)
    yhat=p(x)
    ybar=np.mean(y)
    ssreg=np.sum((yhat-ybar)**2)
    sstot=np.sum((y-ybar)**2)
    # 计算R平方值
    results['determination']=ssreg/sstot
    return results

X_Test=[1,3,8,7,9]
Y_Test=[10,12,24,21,34]
print(computeCorrelation(X_Test,Y_Test))
print(computeCorrelation(X_Test,Y_Test)**2)
print(polyfit(X_Test,Y_Test,1)['determination'])