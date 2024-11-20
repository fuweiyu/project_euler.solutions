def sum_of_divisors(n):
    """Returns the sum of proper divisors of n."""
    total = 1  # 1 is always a divisor
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:  # Avoid adding the square root twice for perfect squares
                total += n // i
    return total

def is_abundant(n):
    """Checks if a number is abundant."""
    return sum_of_divisors(n) > n

def generate_abundant_numbers(limit):
    """Generates a list of all abundant numbers up to a given limit."""
    return [n for n in range(12, limit) if is_abundant(n)]

def calculate_non_abundant_sum(limit):
    """Calculates the sum of all positive integers not writable as the sum of two abundant numbers."""
    abundant_numbers = generate_abundant_numbers(limit)
    abundant_sums = [False] * (limit + 1)  # Boolean array to mark sums of two abundant numbers
    
    # Mark all numbers that can be written as the sum of two abundant numbers
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            abundant_sum = abundant_numbers[i] + abundant_numbers[j]
            if abundant_sum <= limit:
                abundant_sums[abundant_sum] = True
            else:
                break
    
    # Calculate the sum of numbers not writable as the sum of two abundant numbers
    return sum(i for i in range(limit + 1) if not abundant_sums[i])

# Constants
LIMIT = 28123  # Given in the problem

# Calculate and display the result
result = calculate_non_abundant_sum(LIMIT)
print(f"The sum of all positive integers which cannot be written as the sum of two abundant numbers is: {result}")
