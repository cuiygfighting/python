def fab(n):
    """递归实现斐波那契数列"""
    if n==1 or n==2:
        return 1
    else:
        return fab(n-1)+fab(n-2)

def fab2(n):
    """循环实现斐波那契数列"""
    a=[]
    a.append(0)
    a.append(1)
    for value in range(2,n+1):
        a.append(a[value-1]+a[value-2])
    return a

print(fab2(10))