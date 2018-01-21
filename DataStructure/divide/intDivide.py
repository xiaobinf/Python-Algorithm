def intDivide(n,m):
    '''
    整数划分
    :param n:待划分整数
    :param m: 划分的最大值
    :return:
    '''
    if n==1 or m==1:
        return 1
    if n<m :
        return intDivide(n,n)
    if n==m :
        return intDivide(n,m-1)+1
    if n>m and m>1:
        return intDivide(n-m,m)+intDivide(n,m-1)
    return 0

print(intDivide(5,5))