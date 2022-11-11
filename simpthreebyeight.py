
x0=int(input("Lower limit of the interval:"))
xn=int(input("Upper limit of the interval:"))
n=int(input("Number of sub intervals(Multiples of 3):"))

def f(x):
    return 1/(1+x**2)  #write function here

h=(xn-x0)/n
sum1=f(x0)+f(xn)

for i in range(1,n):
    if(i%3==0):
        sum1=sum1+2*f(x0+i*h)
    else:
        sum1=sum1+3*f(x0+i*h)

print("Estimated value of given integration:",3*h/8*sum1)
    
