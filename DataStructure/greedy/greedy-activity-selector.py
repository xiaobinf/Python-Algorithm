S=[(7,10),(9,12),(8,13),(11,12),(12,16)]
def greedy_activity_selector(S):
    '''
    活动安排 贪心算法 每个活动(si，fi)  开始时间si，结束时间fi
    :param S: S=[(7,10),(9,12),(8,13),(11,12),(12,16)]
    :return:A:活动顺序
    '''
    S=sorted(S,key=lambda s:s[1])
    # S=[(7, 10), (9, 12), (11, 12), (8, 13), (12, 16)]
    A=list()
    A.append(S[0])
    j=0
    for i in range(1,len(S)):
        # S[j]表示前一个任务
        if S[i][0]>=S[j][1]:
            A.append(S[i])
            j=i
    return A


if __name__=='__main__':
    print(greedy_activity_selector(S))