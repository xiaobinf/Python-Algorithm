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

def backtrack(t):
    '''
    n皇后 回溯递归解法 if语句用于保存一个解
    else语句  for i in range(n): 遍历了0..n-1个子树
    x.append(i)  x.pop()这是一个疑惑点 回到父节点的状态？？？
    :param t:
    :return:
    '''
    global count,X,x,n
    if t>=n:
        count+=1
        X.append(x[:])
    else:
        for i in range(n):
            x.append(i)
            if place(t) :
                backtrack(t+1) #一直回溯到找到一个解 或者结束
            x.pop()

# 解的可视化（根据一个解x，复原棋盘。'X'表示皇后）
def show(x):
    global n
    for i in range(n):
        print('.' * (x[i]) + 'Q' + '.'*(n-x[i]-1))

#leetcode51
def output():
    l2=list()
    for x in X:
        l1 = list()
        for i in range(n):
            l1.append(str('.' * (x[i]) + 'Q' + '.'*(n-x[i]-1)))
        l2.append(l1)
    return l2





backtrack(0)
# print(X)
# show(X[0])
# print(count)
l=output()
print(l)