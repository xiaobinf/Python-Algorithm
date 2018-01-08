import numpy as np
def fitSLR(x,y):
    '''
    simpleLinearRegression
    np.mean([...]) 返回平均值
    :param x:
    :param y:
    :return: y=kx+b,(k,b)
    '''
    n=len(x)
    numerator=0
    dinominator=0
    for i in range(n):
        numerator+=(x[i]-np.mean(x))*(y[i]-np.mean(y))
        dinominator+=(x[i]-np.mean(x))**2
    print(numerator,dinominator)
    k=numerator/float(dinominator)
    b=np.mean(y)-k*(np.mean(x))
    return k,b

def predict(x,k,b):
    return k*x+b

x=[1,3,2,1,3]
y=[14,24,18,17,27]
k,b=fitSLR(x,y)
print(predict(6,k,b))
