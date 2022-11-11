z=[0,1,2,3,4]
Z=set(z)
n=len(z)
print(Z)
def addmod(x,y):
    return (x+y)%n

def multmod(x,y):
    return (x*y)%n

#multiplicative identity
flag=1

for i in range(0,n):
    if(multmod(z[1],z[i])==z[i] and multmod(z[i],z[1])==z[i]):
        flag=1
    else:
        flag=0
        break

if(flag==0):
    print("Multiplicative identity does not exist")
    flag1=0
else:
    print("Multiplicative identity is ",1,". Hence given ring is with unity")
    
    
