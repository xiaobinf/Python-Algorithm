import random
def mainElement(S):
    '''
    判断是否有主元素
    :param S:
    :return:
    '''
    x=random.choice(S)
    k=0
    for i in S:
        if x==i:
            k+=1
    if k>(len(S)/2):
        return True
    return False

print(mainElement([1,1,1,1,2]))
