z=[0,1,2,3,4,5]
Z=set(z)
n=len(z)
print(Z)
def addmod(x,y):
    return (x+y)%n

def multmod(x,y):
    return (x*y)%n

flag=0

for i in range(0,n):
    for j in range(0,n):
        if(multmod(z[i],z[j])==0 and z[i]!=0 and z[j]!=0):
            print("Zero divisors are:",z[i]," and ",z[j])
            flag=1
            break

if(flag==1):
    print("Zero divisors exist")
else:
    print("Zero divisors does not exist")
    
    
