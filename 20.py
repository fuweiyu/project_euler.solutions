#Number for determine its factorial
n=100

#Calculation for the factorial of N
fact=1
for i in range (1,int(n+1)):
    fact=fact*i
print(fact)

#Sum of the digits of the factorial
str_fact=str(fact)
sum=0
for j in range (0, len(str_fact)):
    sum+=int(str_fact[j])
print (sum)