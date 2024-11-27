def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def quadratic_primes(limit_a, limit_b):
    """Find coefficients a and b for the quadratic formula that produces the maximum number of primes."""
    max_primes = 0
    product_of_coefficients = 0

    for a in range(-limit_a + 1, limit_a):
        for b in range(-limit_b, limit_b + 1):
            n = 0
            while True:
                quadratic_result = n**2 + a*n + b
                if is_prime(quadratic_result):
                    n += 1
                else:
                    break

            if n > max_primes:
                max_primes = n
                product_of_coefficients = a * b
                best_a, best_b = a, b

    return best_a, best_b, max_primes, product_of_coefficients

# Set the limits for a and b
limit_a = 1000
limit_b = 1000

# Find the result
a, b, max_primes, product = quadratic_primes(limit_a, limit_b)
print(f"The coefficients are a = {a}, b = {b}")
print(f"The maximum number of consecutive primes is {max_primes}")
print(f"The product of the coefficients is {product}")
