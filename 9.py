for i in range (0,1000, 1):
    for j in range (i+1, 1000, 1):
        for k in range (j+1, 1000, 1):
            if (((i*i+j*j)==k*k) and ((i+j+k)==1000)):
                print (i,j,k)
                print (i*j*k)