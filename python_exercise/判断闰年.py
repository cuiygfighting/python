try:
    a=int(input("Please input the year:"))
except:
    pass
else:
    if a%400==0 or (a%4==0 and a%100!=0):
        print("您输入的%10d,%d是闰年。"%(a,a))
    else:
        print("不是闰年")