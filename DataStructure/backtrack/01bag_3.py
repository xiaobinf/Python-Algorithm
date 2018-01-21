'''
回溯法解决01背包问题 提取成conflict函数 具有一般性
'''
bestV,bestx = 0,None
curW ,curV = 0 , 0
n ,c = 5,12
w = [2, 2, 6, 5, 4]
v = [6, 3, 5, 4, 6]
x = [0 for i in range(n)]



def conflict(k,i):
    if w[k]*i+curW>c:
        return True
    return False


def backtrack(k):
    global bestV, curV, x, bestx, curW, w, v
    if k>=n:#满足回溯终止条件
        if curV>bestV:
            bestV=curV
            bestx=x[:]
    else:
        for i in (0,1):#遍历子节点
            x[k] = i
            if not conflict(k,i):
                # x[k]=i
                curV+=v[k]*i
                curW+=w[k]*i
                backtrack(k+1)
                curW-=w[k]*i
                curV-=v[k]*i

backtrack(0)
print(bestV)
print(curW,curV)
print(bestx)