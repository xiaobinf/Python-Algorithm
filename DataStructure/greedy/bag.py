# 选择单位体积内价值最高的 物品可以分割
S=[(30,100,1),(20,120,2),(70,10,3),(10,50,4)]

C=100

def bag(S,C):
    '''
    :param S: S=[(W,P),...]
    :param C:bag content
    :return: A:[(id,个数),(id,个数),...]
    '''
    S=sorted(S, key=lambda s: s[1] / s[0], reverse=True)
    # [(20, 120,2), (10, 50,4), (30, 100,1), (70, 10,3)]
    A=list()
    for i in range(len(S)):
        if S[i][0]<C:
            C-=S[i][0]
            A.append((S[i][2],1))
        else:
            if C>0:
                A.append((S[i][2],C/S[i][0]))
                break
    print(A)

bag(S,100)
