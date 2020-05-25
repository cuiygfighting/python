import math
def max_num(n1,n2):
    """最大公约数"""
    if n1>n2:
        smaller=n2
    else:
        smaller=n1
    key=0
    for num in range(1,smaller+1):
        if n1%num==0 and n2%num==0:
            key=num
    print("%d和%d的最大公约数为：%d"%(n1,n2,key))

def min_num(n1,n2):
    """最小公倍数"""
    if n1 < n2:
        bigger = n2
    else:
        bigger = n1
    while 1:
        if bigger % n1 == 0 and bigger % n2 == 0:
            break
        bigger+=1
    print("{}和{}的最小公倍数为：{}".format(n1,n2,bigger))


max_num(36,90)
print(math.gcd(36,90))
min_num(36,57)
print((36*57)//math.gcd(36,57))