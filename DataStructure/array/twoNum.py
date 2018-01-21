def twoNum_1():
    a = [1, 2, 4, 3, 5, 6, 8, 7]
    num = 14
    b = sorted(a)
    print(b)
    i = 0
    j = len(a) - 1
    while i < j:
        if b[i] + b[j] == num:
            print(b[i], b[j], i, j)
            break
        elif b[i] + b[j] > num:
            j -= 1
        else:
            b[i] + b[j] < num
            i += 1

def twoNum_2():
    a = [1, 2, 4, 3, 5, 6, 8, 7]
    num = 15
    d={}
    k=0
    # construct dict
    for i in a:
        d[i]=k
        k+=1
    print(d)
    for i in a:
        if num-i in d:
            print('i:{},j:{}'.format(i,num-i))
            break
        else:
            continue

if __name__ == '__main__':
    twoNum_2()