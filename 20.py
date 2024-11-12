from math import factorial

# Step 1: Calculate 100!
factorial_100 = factorial(100)

# Step 2: Convert to string and sum the digits
sum_of_digits = sum(int(digit) for digit in str(factorial_100))
sum_of_digits
print (sum_of_digits)