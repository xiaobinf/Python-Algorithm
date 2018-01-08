from numpy import genfromtxt
import numpy as np
from sklearn import linear_model,datasets

# 多元线性回归分析  X数据类型增加了类型信息  类型信息相应转化为数组
# r  raw原始字符
deliveryData=genfromtxt(r"Delivery_Dummy.csv",delimiter=',')
print(deliveryData)
X=deliveryData[:,:-1]
print('X:',X)
Y=deliveryData[:,-1]
print('Y:',Y)

regr=linear_model.LinearRegression()
regr.fit(X,Y)

print(regr.coef_)
print(regr.intercept_)

xPred=np.mat([102,6,0,0,1])
pPred=regr.predict(xPred)
print(pPred)


