from numpy import genfromtxt
import numpy as np
from sklearn import linear_model,datasets

# 多元线性回归分析
# r  raw原始字符
deliveryData=genfromtxt(r"Delivery.csv",delimiter=',')
print(deliveryData)
X=deliveryData[:,:-1]
print('X:',X)
Y=deliveryData[:,-1]
print('Y:',Y)

regr=linear_model.LinearRegression()
regr.fit(X,Y)

print(regr.coef_)
print(regr.intercept_)

xPred=np.mat([102,6])
pPred=regr.predict(xPred)
print(pPred)


