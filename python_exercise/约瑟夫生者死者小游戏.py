"""30 个人在一条船上，超载，需要 15 人下船。
于是人们排成一队，排队的位置即为他们的编号。
报数，从 1 开始，数到 9 的人下船。
如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？"""
people=[0]
for n in range(1,31):
    people.append(n)
count=30
flag=0
while count>=16:
    for n in range(1,31):
        if (people[n])!=0:
            flag+=1
            if flag==9:
                print("%d号被踢下船"%people[n])
                people[n]=0
                flag=0
                count-=1



