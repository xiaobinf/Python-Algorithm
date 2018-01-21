'''

'''
S=[1,2,4,4,2,3,3,4,4,4,4,4,4,4]
def majority_1(S):
    '''
    在数组中找主元素 主元素出现的个数>n/2
    :param S:
    :return:主元素，主元素个数
    '''
    cnt,num=1,S[0]
    for i in range(1,len(S)):
        if cnt==0:
            num=S[i]
        if S[i]==num:
            cnt+=1
        else:
            cnt-=1
        count=0
    for i in range(len(S)):
        if S[i]==num:
            count+=1
    return num,count
print(majority_1(S))
