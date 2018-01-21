A,B=[1, 14, 31, 50, 70],[7, 23, 40, 60, 75]
def getLength(A,B):
    '''
    对于有序数组A,B 返回A,B元素之间最小的距离 O(n)算法
    参看：https://yq.aliyun.com/wenji/72268
    :param A:
    :param B:
    :return:
    '''
    A_Index,B_Index=0,0
    shortLength=1e9
    while A_Index<len(A) and B_Index<len(B):
        if A[A_Index]>B[B_Index]:
            shortLength=min(shortLength,A[A_Index]-B[B_Index])
            B_Index+=1
        else:
            shortLength=min(shortLength,B[B_Index]-A[A_Index])
            A_Index+=1
    return shortLength
print(getLength(A,B))

