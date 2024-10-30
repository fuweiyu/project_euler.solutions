p=1
i=0
while p<=10001:
    c=0
    #print (i)
    for j in range (1, i, 1):
        if (i%j==0):
            c=c+1
    if (c==1):
        #print (p, ": ",i)
        p+=1
    i+=1
print (p-1, ": ",i-1)