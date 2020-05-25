import matplotlib.pyplot as plt
x=list(range(1,100))
y=[(x1)**2 for x1 in x]
plt.scatter(x,y,c=y,cmap=plt.cm.Reds,edgecolor='none',s=40)
plt.title("Squares Number",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square value",fontsize=14)

plt.tick_params(axis='both',which='major',labelsize=14)
plt.axis([0,110,0,11000])
plt.savefig('squares_plot.png')

plt.show()