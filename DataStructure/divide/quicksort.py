def quickSort_0(a):
    '''
    python的列表推导 快速排序  可以继续用随机算法优化
    :param a:
    :return:
    '''
    if a==[]:
        return a
    else:
        key=a[0]
        return quickSort_0([i for i in a if i<key])+[i for i in a if i==key]+quickSort_0([i for i in a if i>key])

def quickSort_1(a,low,high):
    '''
    快速排序 修改原列表版本
    :param a:
    :param low:
    :param high:
    :return:
    '''
    if low<high:
        pivot=partion(a,low,high)
        quickSort_1(a,low,pivot-1)
        quickSort_1(a,pivot+1,high)

def partion(a,low,high):
    pivotkey = a[high]
    print(pivotkey)
    while low<high:
        while low<high and a[low]<=pivotkey:
            low+=1
        a[low],a[high]=a[high],a[low]
        while low<high and a[high]>=pivotkey:
            high-=1
        a[low], a[high] = a[high], a[low]
    print(a)
    return low
a=[2,8,7,1,3,5,6,4]
quickSort_1(a,0,7)
print(a)

b=[1]
quickSort_1(b,0,0)
print(b)
















