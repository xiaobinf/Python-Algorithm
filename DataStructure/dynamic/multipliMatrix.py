def multipliMatrix(r):
    '''
    矩阵连乘算法
    :param r:
    :return:
    '''
    n=len(r)
    m=[[1e9 for i in range(n)] for j in range(n)]
    s = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        m[i][i]=0
    # print(m)
    # d为差距 i和j之间距离
    for d in range(1,n-1):
        for i in range(1,n-d):
            j=i+d
            # m[i][j]=1e9
            for k in range(i,j):
                # r=[30,35,15,5,10,20,25]
                q = m[i][k] + m[k + 1][j] + r[i - 1] * r[k] * r[j]
                if q < m[i][j]:
                    m[i][j] = q
                    # s[i][j]=k 记录位置
                    s[i][j] = k
    print('路径数组s：',s)
    PRINT_OPTIMAL_PARENS(s, 1, n - 1)
    print()
    return m

def PRINT_OPTIMAL_PARENS(s, i, j):
    if i == j:
        print('A', end = '')
        print(i, end = '')
    else:
        print('(', end = '')
        PRINT_OPTIMAL_PARENS(s, i, s[i][j])
        PRINT_OPTIMAL_PARENS(s, s[i][j]+1, j)
        print(')', end = '')


# 4个矩阵
print(multipliMatrix([10,20,50,1,100]))
print(multipliMatrix([10,100,5,50]))
print(multipliMatrix([30,35,15,5,10,20,25]))
