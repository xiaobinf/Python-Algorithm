import matplotlib.pyplot as plt
import pickle
from numpy import *


def loadDataSet(fileName):
    dataMat=[]
    fr=open(fileName)
    for line in fr.readlines():
        curLine=line.strip().split('\t')
        fltLine=array(curLine).astype(float)
        dataMat.append(fltLine)
    return mat(dataMat)



fr=open('pickle.txt','rb')
centroids=pickle.load(fr)
clusterAssment=pickle.load(fr)
fr.close()

color = ['b','y','k','g']

dataMat=loadDataSet('testSet2.txt')
for i in range(shape(dataMat)[0]):
    plt.scatter(array(dataMat[:,0])[i],array(dataMat[:,1])[i],c=color[int(clusterAssment[:,0][i])])


print([i[0] for i in array(centroids[:,0])],[i[0] for i in array(centroids[:,1])])
plt.scatter([i[0] for i in array(centroids[:,0])],[i[0] for i in array(centroids[:,1])],c='r',marker='P')
plt.show()
