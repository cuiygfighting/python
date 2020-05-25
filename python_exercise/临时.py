x=10000
y=0.028
n=12
sum=n*(x*y*(1+y)**n)/((1+y)**n-1)
sum2=x+x*y*(n+1)/2
print(sum)
print(sum2)