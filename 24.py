from math import factorial

def find_lexicographic_permutation(digits, n):
    # List to store the result
    result = []
    # Convert digits into a list for manipulation
    digits = sorted(digits)
    # Adjust n to zero-based indexing
    n -= 1

    while digits:
        # Find the size of each block in the current position
        block_size = factorial(len(digits) - 1)
        # Determine the index of the current digit
        index = n // block_size
        # Append the chosen digit to the result
        result.append(digits.pop(index))
        # Update n to the remainder for the next position
        n %= block_size

    return ''.join(map(str, result))

# Input digits and the target permutation index
digits = list(range(10))  # Digits 0 through 9
n = 1_000_000  # Millionth permutation

# Find and print the result
result = find_lexicographic_permutation(digits, n)
print(f"The millionth lexicographic permutation is: {result}")
