def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_truncatable_prime(num):
    """Check if a number is truncatable from both left to right and right to left."""
    if num < 10:  # Single-digit primes are not considered
        return False
    
    # Check truncations from left to right
    num_str = str(num)
    for i in range(len(num_str)):
        if not is_prime(int(num_str[i:])):  # Remove digits from the left
            return False

    # Check truncations from right to left
    for i in range(1, len(num_str)):
        if not is_prime(int(num_str[:i])):  # Remove digits from the right
            return False

    return True

def find_truncatable_primes():
    """Find the sum of all 11 truncatable primes."""
    truncatable_primes = []
    num = 11  # Start checking from 11 as single-digit primes are excluded

    while len(truncatable_primes) < 11:
        if is_prime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
        num += 2  # Skip even numbers

    return truncatable_primes, sum(truncatable_primes)

# Find and print the sum of all truncatable primes
truncatable_primes, total_sum = find_truncatable_primes()
print(f"The truncatable primes are: {truncatable_primes}")
print(f"The sum of all truncatable primes is {total_sum}.")
