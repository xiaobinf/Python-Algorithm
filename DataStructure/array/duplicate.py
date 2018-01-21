def duplicate(l):
    '''
    找出数组中任意一个重复的数字
    :param l:
    :return:
    '''
    for i in range(len(l)):
        while l[i]!=i:
            if l[i]==l[l[i]]:
                return True,l[i]
            l[l[i]],l[i]=l[i],l[l[i]]
    return False

if __name__=='__main__':
    print(duplicate([2,3,1,0,2,5,3]))