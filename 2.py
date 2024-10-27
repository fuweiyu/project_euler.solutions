#we generate a list
fibonacci=list()

#append the first two terms to the list
fibonacci.append(1)
fibonacci.append(2)

#the firs even term is 2 so we initiate the sum with it
sum_terms=(fibonacci[1])

for i in range (2,100,1):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

    #Test print of the fibonacci numbers
    #print (fibonacci[i])

    #Evaluate the conditions to add these terms or end the loop
    if (fibonacci[i]<4000000 and fibonacci[i]%2==0):
        sum_terms=(sum_terms + fibonacci[i])
    else:
        if (fibonacci[i]>=4000000):
            break

#print the result we have found:
print(sum_terms)