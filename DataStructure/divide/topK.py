def selectTopK(a,low,high,k):
    '''
    选择数组的第k大的元素 k是数组的一个下标
    类似快速排序的分治法 先选择一个固定位置
    :param a:
    :param low:
    :param high:
    :param k:
    :return:
    '''
    if low==high and k==0:
        return a[0]
    pivotkey=a[high]
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
    # return i  parttition函数
    if k<i:
        return selectTopK(a,low,i-1,k)
    elif k>i:
        return selectTopK(a,i+1,high,k)
    else:
        return a[i]

print(selectTopK([1,5,3,4,2,3],0,5,3))