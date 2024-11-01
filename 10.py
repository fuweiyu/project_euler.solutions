import math
p=0
i=2
while i<2000000:
    c=0
    for j in range (1,int(math.sqrt(i))+1, 1):
        if (i%j==0):
            c=c+1
    if (c==1):
        p=p+i
        #print (i)
    i+=1
print ("sum:"+str(p))