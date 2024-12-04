from itertools import permutations

def is_pandigital(identity):
    """Check if the given identity is a 1 through 9 pandigital."""
    return ''.join(sorted(identity)) == "123456789"

def find_pandigital_products():
    """Find the sum of all unique products that are pandigital."""
    products = set()  # To store unique products

    # Iterate through possible permutations of the digits 1 through 9
    digits = "123456789"
    for perm in permutations(digits):
        perm = ''.join(perm)

        # Check for valid split positions
        for split1 in range(1, 5):  # Splitting for multiplicand (max 4 digits)
            for split2 in range(split1 + 1, 8):  # Splitting for multiplier (max 4 digits)
                multiplicand = int(perm[:split1])
                multiplier = int(perm[split1:split2])
                product = int(perm[split2:])
                
                if multiplicand * multiplier == product:
                    products.add(product)

    return sum(products)

# Calculate the sum of all such pandigital products
result = find_pandigital_products()
print(f"The sum of all pandigital products is {result}.")
