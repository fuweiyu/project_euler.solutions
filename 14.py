num=2
terms=0
collatz_sequence=""
longest=0
starting_number=0
for i in range (2, 1000000,1):
    num=i
    terms=1
    collatz_sequence=(str(int(num))+"→")
    while (num>1):
        if (num%2==0):
            num=num/2
            terms=terms+1
            if (num==1):
                collatz_sequence=collatz_sequence+(str(int(num)))
            else:
                collatz_sequence=collatz_sequence+(str(int(num))+"→")
        if (num!=1 and num%2==1):
            num=num*3+1
            terms=terms+1
            collatz_sequence=collatz_sequence+(str(int(num))+"→")
    print (collatz_sequence)
    print("number of terms: "+str(terms)+"\n")
    if (terms>longest):
        longest=terms
        starting_number=i
print("the longest sequence have "+str(longest)+" terms and it is started by "+str(starting_number))