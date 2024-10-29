import math
sum_of_squares=0
sums=0
for i in range (1,101,1):
    sum_of_squares = sum_of_squares + pow(i,2)
    sums=sums+i
square_of_sums = pow (sums,2)
print (square_of_sums-sum_of_squares)