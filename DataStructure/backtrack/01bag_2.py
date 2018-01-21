bestV,bestx = 0,None
curW ,curV = 0 , 0
n ,c = 5,12
w = [2, 2, 6, 5, 4]
v = [6, 3, 5, 4, 6]
x = [0 for i in range(n)]
def backtrack(t):
    global bestV,curV,x,bestx,curW,w,v
    if t>=n:
        if bestV<curV:
            bestV=curV
            bestx=x[:]
    else:
        for i in (0,1):
            x[t] = i
            if i==0:
                backtrack(t+1)
            else:
                if w[t]+curW<=c:
                    curW+=w[t]
                    curV+=v[t]
                    backtrack(t+1)
                    curW-=w[t]
                    curV-=v[t]
backtrack(0)
print(bestV)
print(curW,curV)
print(bestx)


