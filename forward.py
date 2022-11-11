x=[1,2,3,4,5]
print("x values:",x)
y=[10,26,58,112,194]
print("y values:",y)
X=1.4
n=len(x)
h=x[1]-x[0]
p=(X-x[0])/h
sum1=y[0]
term=1
print("Difference table:")
for i in range(1,n-1):
    print(end="\n")
    for j in range(0,n-i):
        y[j]=y[j+1]-y[j]
        print(y[j],end="\t")
    term=term*(p-i+1)/i
    sum1=sum1+term*y[0]

print("\nthe value of f(1.4):",sum1)
    
