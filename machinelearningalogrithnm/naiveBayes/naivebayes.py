from collections import Counter
'''
来自统计学习方法
'''
X=[[1,'S'],[1,'M'],[1,'M'],[1,'S'],[1,'S'],[2,'S'],\
[2,'M'],[2,'M'],[2,'L'],[2,'L'],[3,'L'],[3,'M'],[3,'M'],[3,'L'],[3,'L']]

Y=[-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1]

x=[2,'S']

def naivebayes_classify(X,Y,x):
    '''
    bayes分类
    :param X:训练数据
    :param Y:训练数据标签
    :param x:实例x
    :return: 返回分类
    '''
    # 字典组成的counter对象
    count=Counter(Y)
    # 计算先验概率
    pt=count.get(1)/len(Y)
    pf=count.get(-1)/len(Y)
    # y=1的index
    idxt=[i for i in range(len(Y)) if Y[i]==1]
    # y=-1的index
    idxf=[i for i in range(len(Y)) if Y[i]==-1]

    d1={1:0,2:0,3:0}
    for i in idxt:
        if X[i][0]==1:
            print('...')
            d1[1]+=1
        if X[i][0]==2:
            d1[2]+=1
        if X[i][0]==3:
            d1[3]+=1
    print(d1)
    # p(x1=.,y=1)
    pxy11=d1[1]/len(idxt)
    pxy21=d1[2]/len(idxt)
    pxy31=d1[3]/len(idxt)
    print(pxy11,pxy21,pxy31)

    d2 = {1: 0, 2: 0, 3: 0}
    for i in idxf:
        if X[i][0] == 1:
            d2[1] += 1
        if X[i][0] == 2:
            d2[2] += 1
        if X[i][0] == 3:
            d2[3] += 1
    print(d2)
    # p(x1=.,y=-1)
    pxy10 = d2[1] / len(idxf)
    pxy20 = d2[2] / len(idxf)
    pxy30 = d2[3] / len(idxf)
    print(pxy10, pxy20, pxy30)

    d3={'S':0,'M':0,'L':0}
    for i in idxt:
        if X[i][1]=='S':
            d3['S']+=1
        if X[i][1]=='M':
            d3['M']+=1
        if X[i][1]=='L':
            d3['L']+=1
    print(d3)
    # x2=. y=1
    pxys1=d3['S']/len(idxt)
    pxym1=d3['M']/len(idxt)
    pxyl1=d3['L']/len(idxt)
    print(pxys1,pxym1,pxyl1)

    d4 = {'S': 0, 'M': 0, 'L': 0}
    for i in idxf:
        if X[i][1] == 'S':
            d4['S'] += 1
        if X[i][1] == 'M':
            d4['M'] += 1
        if X[i][1] == 'L':
            d4['L'] += 1
    print(d4)
    # x2=. y=-1
    pxys0 = d4['S'] / len(idxf)
    pxym0 = d4['M'] / len(idxf)
    pxyl0 = d4['L'] / len(idxf)
    print(pxys0, pxym0, pxyl0)
    # 分类
    if x[0]==1 and x[1]=='S':
        p1 = pt * pxy11 * pxys1
        p2 = pf * pxy10 * pxys0
    if x[0] == 1 and x[1] == 'M':
        p1 = pt * pxy11 * pxym1
        p2 = pf * pxy10 * pxym0
    if x[0] == 1 and x[1] == 'L':
        p1 = pt * pxy11 * pxyl1
        p2 = pf * pxy10 * pxyl0
    if x[0] == 2 and x[1] == 'S':
        p1 = pt * pxy21 * pxys1
        p2 = pf * pxy20 * pxys0
    if x[0] == 2 and x[1] == 'M':
        p1 = pt * pxy21 * pxym1
        p2 = pf * pxy20 * pxym0
    if x[0] == 2 and x[1] == 'L':
        p1 = pt * pxy21 * pxyl1
        p2 = pf * pxy20 * pxyl0
    if x[0] == 3 and x[1] == 'S':
        p1 = pt * pxy31 * pxys1
        p2 = pf * pxy30 * pxys0
    if x[0] == 3 and x[1] == 'M':
        p1 = pt * pxy31 * pxym1
        p2 = pf * pxy30 * pxym0
    if x[0] == 3 and x[1] == 'L':
        p1 = pt * pxy31 * pxyl1
        p2 = pf * pxy30 * pxyl0
    print(p1,p2)

    if p1>p2:
        return 1
    else:
        return -1






if __name__=='__main__':
    print(naivebayes_classify(X,Y,(3,'M')))