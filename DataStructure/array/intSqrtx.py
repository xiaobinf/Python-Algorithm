def mySqrt(x):
    """
    暴力搜索 超时
    :type x: int
    :rtype: int
    """
    rt=0
    pows=[i**2 for i in range(x+2)]
    for i in range(x+1):
        if pows[i]<=x and pows[i+1]>x:
            rt=i
            break
    return rt

def mySqrt_1(x):
    left,right=1,x
    while(left<=right):
        mid=left+(right-left)//2
        if mid==x//mid:
            return mid
        elif mid<x//mid:
            left=mid+1
        else:
            right=mid-1
    return right
def mySqrt_2(x):
    left,right=0,x
    if x==1: return 1
    if x==0: return 0
    mid=x//2
    while left<=right:
        if mid**2<=right:
            left=mid+1
        else :
            right=mid-1
        mid=(right+left)//2
    return mid
print(mySqrt_2(70))