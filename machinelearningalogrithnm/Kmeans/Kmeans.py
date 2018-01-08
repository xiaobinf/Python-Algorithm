from numpy import *
def loadDataSet(fileName):
    dataMat=[]
    fr=open(fileName)
    for line in fr.readlines():
        curLine=line.strip().split('\t')
        fltLine=array(curLine).astype(float)
        dataMat.append(fltLine)
    return mat(dataMat)

def distEclud(vecA,vecB):
    return sqrt(sum(power(vecA-vecB,2)))

def randCent(dataSet,k):
    n=shape(dataSet)[1]
    # centroids k个质心
    centroids=mat(zeros((k,n)))
    for j in range(n):
        minJ=min(dataSet[:,j])
        rangeJ=float(max(dataSet[:,j])-minJ)
        # dataSet矩阵中每一列最小值 加上一个范围 产生的k个点不超过dataSet
        centroids[:,j]=minJ+rangeJ*random.rand(k,1)
    return centroids

def KMeans(dataSet,k,distMeas=distEclud,createCent=randCent):
    m=shape(dataSet)[0]
    clusterAssment=mat(zeros((m,2)))
    centroids=createCent(dataSet,k)
    clusterChanged=True
    while clusterChanged:
        clusterChanged=False
        for i in range(m):
            minDist=inf;
            minIndex=-1
            for j in range(k):
                distJI=distMeas(centroids[j,:],dataSet[i,:])
                if distJI<minDist:
                    minDist=distJI
                    minIndex=j
            if clusterAssment[i,0]!=minIndex:
                clusterChanged=True
            clusterAssment[i,:]=minIndex,minDist**2
        print(centroids)
        for cent in range(k):
            ptsInClust=dataSet[nonzero(clusterAssment[:,0].A==cent)[0]]
            centroids[cent,:]=mean(ptsInClust,axis=0)
    return centroids,clusterAssment


def biKMeans(dataSet,k,distMeas=distEclud):
    pass


if __name__=="__main__":
    # f=open("testSet.txt",'r')
    # print(numpy.array(f.readline().split()).astype(float))
    dataMat=loadDataSet("testSet2.txt")
    print(dataMat)
    centroids,clusterAssment=KMeans(dataMat,4)
    import pickle
    fw=open('pickle.txt','wb')
    pickle.dump(centroids,fw)
    pickle.dump(clusterAssment,fw)
    fw.close()
    print(KMeans(dataMat,4))



