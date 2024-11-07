#first part: calculate the power of 2
power=1
for i in range (0,1000,1):
    power=power*2
print(power)
result=str(power)

#second part: calculate the sum of the digits of the resul of part 1
sum=0
for j in range (0,int(len(result)),1):
    sum= sum + int(result[j])
print(sum)

