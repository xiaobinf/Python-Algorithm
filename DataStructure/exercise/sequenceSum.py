def seqSum(x,n,p):
    sum=0
    for i in range(n):
        sum+=x**i
    return sum%p

print(seqSum(1095,1092,3))