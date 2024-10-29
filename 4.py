import math

def reverse(num):
    rev=0
    i=0
    while num >0:
        rev=rev*10+num%10
        num=num//10
        i=i+1
    return (rev)

pal=0
for i in range (100,1000, 1):
    for j in range (i, 1000, 1):
        #print(i,"x",j,"=", i*j)
        if (i*j==reverse(i*j) and i*j> pal):
            pal=i*j
print (pal)

