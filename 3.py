import math
num=600851475143
for i in range (2, int(math.sqrt(num)), 1):
    c=0
    #print (i)
    for j in range (1, i, 1):
        if (i%j==0):
            c=c+1
    if (c==1):
        if (num%i==0):
            print (i)
