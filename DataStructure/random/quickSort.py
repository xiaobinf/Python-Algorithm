import random
S=[7,3,2,4,5,7,9,6,7,9,11,2,33,56,32]
random.shuffle(S)
def quickSort(S):
    '''
    快速排序 采用sherwood随机算法 避免最坏情况出现
    :param S:
    :return:
    '''
    if S==[]:
        return []
    num=random.choice(S)
    return quickSort([i for i in S if i<num])+[i for i in S if i==num]+quickSort([i for i in S if i > num])

def quickSort_1(S):
    '''
    将乱序数组去除重复元素，并且排序
    :param S:
    :return:
    '''
    if S==[]:
        return []
    num=random.choice(S)
    return quickSort_1([i for i in S if i<num])+[num]+quickSort_1([i for i in S if i>num])

def quickSort_2(a,low,high):
    '''
    快速排序 修改原列表版本
    :param a:
    :param low:
    :param high:
    :return:
    '''
    if low<high:
        pivot=partition_2(a,low,high)
        quickSort_2(a,low,pivot-1)
        quickSort_2(a,pivot+1,high)

def partion_r(a,low,high):
    # pivotkey = random.choice(a[low:high+1])
    # 产生[low,high]随机数 包括high
    i=random.randint(low,high)
    pivotkey=a[i]
    print(pivotkey)
    # 把选择的随机数放在数组末尾
    a[high],a[i]=a[i],a[high]
    while low<high:
        while low<high and a[low]<=pivotkey:
            low+=1
        a[low],a[high]=a[high],a[low]
        while low<high and a[high]>=pivotkey:
            high-=1
        a[low], a[high] = a[high], a[low]
    print(low,high)
    print(a)
    return low


def partion(a,low,high):
    '''
    直接选最右边作为pivotkey
    :param a:
    :param low:
    :param high:
    :return:
    '''
    pivotkey=a[high]
    print(pivotkey)
    while low<high:
        while low<high and a[low]<=pivotkey:
            low+=1
        a[low],a[high]=a[high],a[low]
        while low<high and a[high]>=pivotkey:
            high-=1
        a[low], a[high] = a[high], a[low]
    print(low,high)
    print(a)
    return low

def partition_2(a,low,high):
    '''
    算法导论7.1节 划分方法
    :param a:
    :param low:
    :param high:
    :return:
    '''
    pivotkey=a[high]
    i=low-1
    for j in range(low,high):
        if a[j]<=pivotkey:
            i+=1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[high]=a[high],a[i+1]
    print("每一遍划分过程：",a)
    return i+1

# print(quickSort(S))

a=[2,8,7,1,3,5,6,4,4]
a1=[2,4,7,5,3,1,7,8,8,5]
quickSort_2(a1,0,9)
print(a1)
