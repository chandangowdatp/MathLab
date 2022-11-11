z=[0,1,2,3,4]
Z=set(z)
n=len(z)
print(Z)
def addmod(x,y):
    return (x+y)%n

def multmod(x,y):
    return (x*y)%n

#Checking weather set is commutative or not
for i in z:
    for j in z:
        if(multmod(i,j)==multmod(j,i)):
            flag=1
        else:
            flag=0
            break

if(flag==0):
    print("Abelian property fails under multiplication")
else:
    print("Abelian property is satisfied under multiplication")
    
