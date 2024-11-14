def sopd(n):
    sum = 0
    #print("d("+str(i)+"): ", end="")
    for j in range(1, n):
        if n % j == 0:
            sum += j
            #print(str(j)+", ", end="")
    #print("= "+str(sum))
    return sum

sum_an = 0
sums = []

for i in range(1, 10001):
    #print("d(" + str(i) + ")=" + str(sopd(i)))
    sums.append(sopd(i))

for i in range(1, len(sums) + 1):  
    k = sums[i - 1]
    if k>i and k < 10000 and k != i and sopd(k) == i: 
        print("d(" + str(i) + ")=" + str(k) + ", d(" + str(k) + ")=" + str(i))
        sum_an += i + k

print("sum of amicable numbers:", sum_an)
