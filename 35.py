def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_rotations(num):
    """Generate all rotations of a number."""
    s = str(num)
    return {int(s[i:] + s[:i]) for i in range(len(s))}

def find_circular_primes(limit):
    """Find all circular primes below a given limit."""
    primes = {n for n in range(2, limit) if is_prime(n)}
    circular_primes = set()

    for prime in primes:
        rotations = get_rotations(prime)
        if rotations.issubset(primes):  # Check if all rotations are prime
            circular_primes.update(rotations)

    return len(circular_primes)

# Find the number of circular primes below one million
limit = 1_000_000
result = find_circular_primes(limit)
print(f"The number of circular primes below {limit} is {result}.")
