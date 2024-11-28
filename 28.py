def spiral_diagonal_sum(size):
    """
    Calculate the sum of the numbers on the diagonals in a size x size spiral.
    The size must be an odd number.
    """
    if size % 2 == 0:
        raise ValueError("Size must be an odd number.")

    diagonal_sum = 1  # Start with the center of the spiral (1)
    current_number = 1

    for layer in range(1, (size // 2) + 1):
        step = 2 * layer
        for _ in range(4):  # Four corners per layer
            current_number += step
            diagonal_sum += current_number

    return diagonal_sum

# Calculate the sum of the diagonals in a 1001x1001 spiral
size = 1001
result = spiral_diagonal_sum(size)
print(f"The sum of the numbers on the diagonals in a {size}x{size} spiral is {result}.")
