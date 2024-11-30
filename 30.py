def sum_of_fifth_powers():
    """
    Find the sum of all numbers that can be written as the sum of the fifth powers of their digits.
    """
    power = 5
    limit = (9 ** power) * 6  # Reasonable upper limit
    result = 0

    for num in range(2, limit + 1):  # Start from 2 (1 is not included)
        if num == sum(int(digit) ** power for digit in str(num)):
            result += num

    return result

# Find the sum of all such numbers
result = sum_of_fifth_powers()
print(f"The sum of all numbers that can be written as the sum of fifth powers of their digits is {result}.")
