import math

# Function to calculate the number of divisors
def count_divisors(n):
    count = 0
    root = int(math.sqrt(n))
    for i in range(1, root + 1):
        if n % i == 0:
            count += 2 if i != n // i else 1
    return count

# Function to find the first triangular number with over `limit` divisors
def find_triangular_number_with_divisors(limit):
    n = 1
    while True:
        # Calculate the nth triangular number
        triangular_number = n * (n + 1) // 2
        # Calculate the number of divisors
        divisors_count = count_divisors(triangular_number)
        if divisors_count > limit:
            return triangular_number
        n += 1

# Find the first triangular number with more than 500 divisors
result = find_triangular_number_with_divisors(500)
print("The first triangular number with over 500 divisors is:", result)
