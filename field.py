z=[0,1,2,3,4]
Z=set(z) #Set conversion
Z=Z-{0}  #Set difference
n=len(z)
print(Z)
def addmod(x,y):
    return (x+y)%n

def multmod(x,y):
    return (x*y)%n

flag=1
#Existence of multiplicative inverse
s2=set()
for i in range(1,n):
    for j in range(1,n):
        if(multmod(z[i],z[j])==z[1] and multmod(z[j],z[i])==z[1]):
            s2=s2.union({z[i]})
            print("Multiplicative inverse of ",z[i]," is ",z[j])

print(s2)
if(Z==s2):
    print("Multiplicative inverse exist for nonzero elements. Hence given ring is a field")
else:
    print("Multiplicative inverse does not exist for nonzero elements. Hence given ring is not a field")
    
    
