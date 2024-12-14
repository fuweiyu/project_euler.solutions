def is_palindromic(s):
    """Check if a string is palindromic."""
    return s == s[::-1]

def double_base_palindromes(limit):
    """Find the sum of all numbers palindromic in base 10 and base 2 below a limit."""
    total = 0

    for num in range(limit):
        if is_palindromic(str(num)) and is_palindromic(bin(num)[2:]):  # Check both bases
            total += num

    return total

# Set the limit to 1,000,000
limit = 1_000_000
result = double_base_palindromes(limit)
print(f"The sum of all double-base palindromes below {limit} is {result}.")
