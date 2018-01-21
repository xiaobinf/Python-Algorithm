import random


def selectTopK(a,low,high,k):
    '''
    算法导论9.2
    选择数组的第k大的元素
    类似快速排序的分治法 先选择一个固定位置
    :param a:
    :param low:
    :param high:
    :param k:
    :return:
    '''
    if low==high and k==0:
        return a[low]
    m=random.randint(low,high)
    pivotkey=a[m]
    a[m],a[high]=a[high],a[m]
    # print(pivotkey)
    i,j=low,high
    while i<j:
        while i<j and a[i]<=pivotkey:
            i+=1
        a[i],a[j]=a[j],a[i]
        while i<j and a[j]>=pivotkey:
            j-=1
        a[i], a[j] = a[j], a[i]
    print('i:',i)
    t=i-low+1
    # return i  parttition函数
    #
    if k<t:
        return selectTopK(a,low,i-1,k)
    elif k>t:
        return selectTopK(a,i+1,high,k-t)
    else:
        return a[i]
print(sorted([1,5,3,4,2,3,9]))
print(selectTopK([1,5,3,4,2,3,9],0,6,1))