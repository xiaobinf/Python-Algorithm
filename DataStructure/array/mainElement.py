def getMainElement(A):
    '''
    获取数组的主元素 方法：1.随机算法 期望O(n) 2.   O(n)算法 一次遍历 一次判断   3.找数组的中位数 分治法 算法导论9.2 期望时间O(n) 最坏时间O(n)
    :param A:
    :return:
    '''
    count=0
    ele=A[0]
    for i in A:
        if ele==i:
            count+=1
        else:
            count-=1
            if count<=0:
                ele=i
    n=0
    for i in A:
        if i==ele:
            n+=1
    if n>len(A)/2:
        return ele
    return 'mainElement not found'

print(getMainElement([1,1,1,2,2,2,2,3]))