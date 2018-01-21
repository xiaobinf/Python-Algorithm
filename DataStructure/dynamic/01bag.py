n = 5
c = 12
w = [2, 2, 6, 5, 4]
v = [6, 3, 5, 4, 6]
def bag(n,c,w,v):
    dp=[[-1 for i in range(c+1)] for i in range(n+1)]
    for i in range(c+1):
        dp[0][i]=0
    for i in range(1,n+1):
        for j in range(c+1):
            dp[i][j]=dp[i-1][j]
            if w[i-1]<=j and dp[i][j]<dp[i-1][j-w[i-1]]+v[i-1]:
                dp[i][j]=dp[i-1][j-w[i-1]]+v[i-1]
    return dp

def bag_1(n,c,w,v):
    dp = [[0 for i in range(c + 1)] for i in range(n + 1)]
    for j in range(min(w[-1]-1,c)):
        dp[n][j]=0
    for j in range(w[-1],c+1):
        dp[n][j]=v[-1]
    # n-1 to 2
    for i in range(n-1,1,-1):
        for j in range(min(w[i-1]-1,c)):
            dp[i][j]=dp[i+1][j]
        for j in range(w[i-1],c+1):
            dp[i][j]=max(dp[i+1][j],dp[i+1][j-w[i-1]]+v[i-1])
    if c<w[0]:
        dp[1][c]=dp[2][c]
    else:
        dp[1][c]=max(dp[2][c],dp[2][c-w[0]]+v[0])
    return dp






def show(n,c,w,dp):
    print('最大价值{}'.format(dp[n][c]))
    x=[0]*n
    j=c
    for i in range(1,n+1):
        if dp[i][j]>dp[i-1][j]:
            x[i-1]=1
            j-=w[i-1]
    print(x)

dp=bag_1(n,c,w,v)
print(dp)
# show(n,c,w,dp)
