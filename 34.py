from math import factorial

def digit_factorials():
    """
    Find the sum of all numbers which are equal to the sum of the factorial of their digits.
    """
    # Precompute factorials for digits 0 to 9
    digit_factorial = {str(i): factorial(i) for i in range(10)}

    # Set a reasonable upper limit for search
    # The maximum number is 7 * 9! = 7 * 362,880 = 2,540,160
    upper_limit = sum(digit_factorial[str(9)] for _ in range(7))

    result = 0

    for num in range(10, upper_limit):  # Start from 10 as 1! and 2! are excluded
        if num == sum(digit_factorial[d] for d in str(num)):
            result += num

    return result

# Calculate the result
result = digit_factorials()
print(f"The sum of all numbers which are equal to the sum of the factorial of their digits is {result}.")
