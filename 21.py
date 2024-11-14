for i in range(1,300):
    sum=0
    print("d("+str(i)+"): ", end="")
    for j in range (1, i):
        if (i%j==0):
            sum=sum+j
            print(str(j)+", ", end="")
    print("= "+str(sum))
