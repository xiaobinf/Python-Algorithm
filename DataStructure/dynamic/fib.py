# 递归 建立备忘录方法
p=[0 for i in range(1000)]
def fib_1(n):
    if p[n]>0:
        return p[n]
    if n==1 or n==2:
        return 1
    else :
        p[n]=fib_1(n-1)+fib_1(n-2)
        return p[n]

print(fib_1(100))
print(p)