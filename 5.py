num=20
divisors_count=0
divisors=20
while divisors_count<divisors:
    divisors_count=0
    for i in range (1, divisors+1, 1):
        if (num%i==0):
            divisors_count = divisors_count + 1
        else:
           break
    if (divisors_count==divisors):
        print (num)
    else:
        num=num+1