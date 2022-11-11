import math
x0=int(input("Lower limit of the interval:"))
xn=int(input("Upper limit of the interval:"))
n=int(input("Number of sub intervals:"))

def f(x):
    return math.log(x,10)  #write function here

h=(xn-x0)/n
sum1=f(x0)+f(xn)

for i in range(1,n):
    sum1=sum1+2*f(x0+i*h)

print("Estimated value of given integration:",h/2*sum1)
    
