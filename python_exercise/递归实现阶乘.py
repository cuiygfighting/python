def f1(n):
    if n<=0:
        print("请输入正数")
    elif n==1:
        return 1
    else:
        return n*f1(n-1)
while 9:
    number=int(input("Please input the number:"))
    print("n的阶乘为:",f1(number),'\n')