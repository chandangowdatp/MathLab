z=[0,1,2,3,4]
Z=set(z) 
n=len(z)
print("Z=",Z)
def addmod(x,y):
    return (x+y)%n

def multmod(x,y):
    return (x*y)%n

s1=set()
flag1=1
flag=1

#Closure Property wrt addition
for i in range(0,n):
    for j in range(0,n):
        s1=s1.union({addmod(z[i],z[j])})

print("s1=",s1)
if(Z==s1):
    print("Closure property is satisfied under addition")
else:
    print("Closure property is not satisfied under addition")
    flag1=0
    
#Associative property wrt addtion
for i in range(0,n):
    for j in range(0,n):
        for k in range(0,n):
            if(addmod(addmod(z[i],z[j]),z[k])==addmod(z[i],addmod(z[j],z[k]))):
               flag=1
            else:
                flag=0
                break

if(flag==0):
    print("Associative property fails under addtion")
    flag1=0
else:
    print("Associative property satisfied under addtion")

#Existance of Additive identity
for i in range(0,n):
    if(addmod(z[0],z[i])==z[i] and addmod(z[i],z[0])==z[i]):
        flag=1
    else:
        flag=0
        break

if(flag==0):
    print("Additive identity does not exist")
    flag1=0
else:
    print("Additive identity is",z[0])

#Existance of Additive inverse

s2=set()
for i in range(0,n):
    for j in range(0,n):
        if(addmod(z[i],z[j])==z[0] and addmod(z[j],z[i])==z[0]):
            s2=s2.union({z[i]})
            print("Additive inverse of ",z[i]," is ",z[j])

if(Z==s2):
    print("Inverse Existance property is satisfied")
else:
    print("Inverse Existance property is not satisfied")
    flag1=0
    
#Abelian property wrt addition
for i in range(0,n):
    for j in range(0,n):
        if(addmod(z[i],z[j])==addmod(z[j],z[i])):
            flag=1
        else:
            flag=0
            break

if(flag==0):
    print("Abelian property fails under addtion")
    flag1=0
else:
    print("Abelian property satisfied under addtion")
        

#Closure Property wrt multiplication
for i in range(0,n):
    for j in range(0,n):
        s1=s1.union({multmod(z[i],z[j])})

print("s1=",s1)
if(Z==s1):
    print("Closure property is satisfied under multiplication")
else:
    print("Closure property is not satisfied under multiplication")
    flag1=0

#Associative property wrt multiplication
for i in range(0,n):
    for j in range(0,n):
        for k in range(0,n):
            if(multmod(multmod(z[i],z[j]),z[k])==multmod(z[i],multmod(z[j],z[k]))):
               flag=1
            else:
                flag=0
                break

if(flag==0):
    print("Associative property fails under multiplication")
    flag1=0
else:
    print("Associative property satisfied under multiplication")

if(flag1==1):
    print("Given set with opertation is a ring")
else:
    print("Given set with opertation is not a ring")
