x=[1,2,3,4,5,6,7,8]
print("x values:",x)
y=[1,8,27,64,125,216,343,512]
print("y values:",y)
X=7.5
n=len(x)
h=x[1]-x[0]
p=(X-x[n-1])/h
sum1=y[n-1]
term=1
print("Difference table:")
for i in range(1,n-1):
    print(end="\n")
    for j in range(0,n-i):
        y[j]=y[j+1]-y[j]
        print(y[j],end="\t")
    term=term*(p+i-1)/i
    sum1=sum1+term*y[n-1-i]

print("\nthe value of f(7.5):",sum1)
