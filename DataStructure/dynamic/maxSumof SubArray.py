def maxSumOfSubArray(sums):
    '''
    s ，，s[i]存存放的是sums数组中第i个元素为末尾的最大子段和
    前一段字段和s[i-1]>0 那么可以加上去，使s[i]更大
    :param sums:
    :return:
    '''
    s=[0 for i in range(len(sums))]
    if sums[0]>0:
        s[0]=sums[0]
    for i in range(1,len(sums)):
        if s[i-1]>0:
            s[i]=s[i-1]+sums[i]
        else:
            s[i]=sums[i]
    return s,max(s)

def maxSumOfSubArray_1(sums):
    '''
    优化一下：减少存储空间 max_存放以i结尾的变量 maxOfSum存放最大子序列和
    :param sums:
    :return:
    '''
    maxOfSum,max_=0,0
    for i in range(0,len(sums)):
        if max_>0:
            max_=max_+sums[i]
        else:
            max_=sums[i]
        if max_>maxOfSum:
            maxOfSum=max_
    return maxOfSum

print(maxSumOfSubArray_1([8,-2,2,-1,2,-1,4,-1]))