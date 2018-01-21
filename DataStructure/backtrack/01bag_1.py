bestV = 0
curW = 0
curV = 0
bestx = None


def backtrack(i):
    global bestV, curW, curV, x, bestx
    if i>=n:
        if bestV<curV:
            # 由目标函数减去得不到最优解的子树
            bestV=curV
            bestx=x[:]
    else:
        # if 满足约束条件 w[i]+curW<c  重量约束
        if w[i]+curW<=c:
            # i节点添加进去
            x[i]=True
            curW+=w[i]
            curV+=v[i]
            backtrack(i+1)
            # **回溯 回到原来状态
            curV-=v[i]
            curW-=w[i]
        # 不选择i节点
        x[i]=False
        backtrack(i+1)


if __name__ == '__main__':
    n = 5
    c = 12
    w = [2, 2, 6, 5, 4]
    v = [6, 3, 5, 4, 6]
    x = [False for i in range(n)]
    backtrack(0)
    print(bestV)
    print(bestx)