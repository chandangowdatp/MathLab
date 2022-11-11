x=[5,6,9,11]
print("x values:",x)
y=[12,13,14,16]
print("y values:",y)
X=10
n=len(x)
sum1=0

for i in range(0,n):
    term=1
    for j in range(0,n):
        if(i!=j):
            term=term*(X-x[j])/(x[i]-x[j])
    sum1=sum1+term*y[i]

print("\nEstimated value of f(10):",sum1)
