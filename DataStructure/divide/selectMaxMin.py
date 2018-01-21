def selectMaxMin(a,low,high):
    '''
    分治法选择最大最小元  比较次数3/2n-2次
    :param a:
    :param low:
    :param high:
    :return:
    '''
    if high-low<=1:
        max_=max(a[high],a[low])
        min_=min(a[high],a[low])
        return max_,min_
    max_L,min_L=selectMaxMin(a,low,low+(high-low)//2)
    max_R,min_R=selectMaxMin(a,low+(high-low)//2+1,high)
    return max(max_L,max_R),min(min_L,min_R)

print(selectMaxMin([1,3,-1,4,9,5,2],0,6))