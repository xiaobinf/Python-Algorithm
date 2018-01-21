x=[]
n=8
count=0
X=[]
def place(k):
    '''
    判断如果放置在第k行 是否满足约束条件
    :param k: 8皇后放第k行的约束函数
    :return: true or false
    '''
    global x
    for i in range(k):
        # |为位运算符
        if abs(k-i)==abs(x[k]-x[i]) or x[k]==x[i]:
            return False
    return True

y=[0 for i in range(8)]
def iterBackTrack():
    t=0
    global x,X,n
    while t>=0 :
        y[t]=y[t]+1
        for i in range(8):

            if place(t):
                if t==8:
                    X.append(x[:])
                else:
                    t+=1
        t-=1




# 解的可视化（根据一个解x，复原棋盘。'X'表示皇后）
def show(x):
    global n
    for i in range(n):
        print('. ' * (x[i]) + 'X ' + '. '*(n-x[i]-1))


iterBackTrack()
print(X)
show(X[-1])
print(count)
