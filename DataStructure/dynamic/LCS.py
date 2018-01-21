def LCS(x,y):
    '''
    求最长公共子序列
    :param x: 字符串x
    :param y: 字符串y
    :return: 返回构造数组，转移路径数组，最长公共子序列
    '''
    # 注意x，y构成数组的顺序
    dp=[[0 for i in range(len(y)+1)] for j in range(len(x)+1)]
    prev = [['null' for i in range(len(y) + 1)] for j in range(len(x) + 1)]
    for i in range(1,len(x)+1):
        for j in range(1,len(y)+1):
            # 下标从0开始
            if x[i-1]==y[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
                prev[i][j]=('L_U')
            elif dp[i][j-1]>dp[i-1][j]:
                dp[i][j]=dp[i][j-1]
                prev[i][j]=('L')
            else:
                # 默认相等时 选择上面的
                dp[i][j]=dp[i-1][j]
                prev[i][j]=('U')
    lcs=list()
    # 从后往前 递推 找到一条满足的路径
    i,j=len(x),len(y)
    while i>0 and j>0:
            if prev[i][j]=='L_U':
                lcs.append(x[i-1])
                i-=1
                j-=1
            elif prev[i][j]=='L':
                j-=1
            elif prev[i][j]=='U':
                i-=1
            else:
                break
    print('最长公共子序列：',lcs[::-1])
    return dp,prev,lcs[::-1]

print(LCS('ABCBDAB','BDCABA'))
