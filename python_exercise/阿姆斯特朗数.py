"""num= int(input("请输入一个数字: "))
n=len(str(num)) #这一步很重要，用于判断数字的位数
sum=0
temp=num
while temp>0:
    sum+=(temp%10)**n
    temp//=10
if num==sum:
    print("输入的数是水仙花数")
else:
    print("输入的数不是水仙花数")
"""

def shui_xian_hua(n1,n2):
    """寻找一个范围内的水仙花数"""
    for num in range(n1,n2+1):
        n=len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            sum += (temp % 10) ** n
            temp //= 10
        if num == sum:
            print(num,end=" ")
shui_xian_hua(1,100000)


