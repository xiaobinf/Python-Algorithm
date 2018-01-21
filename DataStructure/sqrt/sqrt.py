def sqrt(n,epsilon=1e-9):
    k=1
    while abs(k**2-n)>epsilon:
        k=(k+n/k)/2
    return k


if __name__=='__main__':
    print(sqrt(3))