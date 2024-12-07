from fractions import Fraction

def find_digit_cancelling_fractions():
    """
    Find all non-trivial digit cancelling fractions and return the denominator
    of their product in lowest terms.
    """
    numerator_product = 1
    denominator_product = 1

    # Iterate over two-digit numbers for numerator and denominator
    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):  # Proper fraction
            n_tens, n_units = divmod(numerator, 10)
            d_tens, d_units = divmod(denominator, 10)

            # Skip cases where digits are invalid for cancelling
            if n_units == 0 and d_units == 0:
                continue

            # Check for digit cancelling conditions
            if n_units == d_tens and d_units != 0:  # Avoid division by zero
                if numerator * d_units == denominator * n_tens:
                    numerator_product *= numerator
                    denominator_product *= denominator

    # Simplify the final fraction
    fraction = Fraction(numerator_product, denominator_product)
    return fraction.denominator

# Calculate the result
result = find_digit_cancelling_fractions()
print(f"The value of the denominator in the lowest terms is {result}.")
