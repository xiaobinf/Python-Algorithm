import random
S=[3,2,4,5,7,9,6,7,9,11,2,33,56,32]
def selectK(k,S):
    '''
    选择第k(k>0)小的元素，随机算法
    :param k:
    :param S:
    :return:
    '''
    num = random.choice(S)
    S1=[i for i in S if i<num]
    S2=[i for i in S if i==num]
    S3=[i for i in S if i>num]
    print(S1,S2,S3,num)
    if len(S1)>=k:
        return selectK(k,S1)
    elif len(S1+S2)>=k:
        # print('second  {}'.format(num))
        # print(num)
        return num
    else:
        return selectK(k-len(S1)-len(S2),S3)
x=selectK(1,S)
print(x)

