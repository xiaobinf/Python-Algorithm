def sqrt_newton(n,epsilon=1e-9):
    '''
    牛顿迭代法开根号 一般对于数值计算g考虑收敛速度
    :param n:
    :param epsilon: 误差范围
    :return:
    '''
    k=2
    while abs(k**2-n)>epsilon:
        k=(k+n/k)/2
    return k


def sqrt_divide(n,epsilon=1e-9):
    '''
    nlogn
    二分法逼近求平方根
    :param n:
    :param epsilon:
    :return:
    '''
    low=0
    high=n
    while low<high:
        mid=low+(high-low)/2
        if abs(mid*mid-n)<epsilon:
            return mid
        else:
            if mid<n/mid:
                low=mid
            else:
                high=mid




if __name__=='__main__':
    print(sqrt_newton(0.1))
    print(sqrt_divide(6))
    import math
    print(math.sqrt(6))