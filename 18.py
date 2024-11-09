# Define the triangle
triangle = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

# Create a copy of the triangle to calculate the path sums without altering the original
triangle_copy = [row[:] for row in triangle]

# Dynamic programming to compute maximum path sum and track the path
path_indices = []
for row in range(len(triangle_copy) - 2, -1, -1):
    for col in range(len(triangle_copy[row])):
        # Add the maximum possible sum from the row below
        if triangle_copy[row + 1][col] > triangle_copy[row + 1][col + 1]:
            triangle_copy[row][col] += triangle_copy[row + 1][col]
        else:
            triangle_copy[row][col] += triangle_copy[row + 1][col + 1]

# The top element now contains the maximum path sum
max_sum = triangle_copy[0][0]

# Track the path from the top to bottom based on the computed sums
index = 0
path_indices.append(index)
for row in range(1, len(triangle_copy)):
    if index + 1 < len(triangle_copy[row]) and triangle_copy[row][index + 1] > triangle_copy[row][index]:
        index += 1
    path_indices.append(index)


# Print the triangle with highlighted maximum path
spaces = len(triangle[-1]) - 1
for i, row in enumerate(triangle):
    print("  " * spaces, end="")  # Center align each row
    for j, value in enumerate(row):
        if path_indices[i] == j:
            color = "\033[31m"  # Red color for the path
            reset = "\033[0m"
            print(f"{color}{value:02}{reset}", end="  ")  # Highlighted value
        else:
            print(f"{value:02}", end="  ")  # Regular values
    print("")
    spaces -= 1
print("\033[31m" + str((path_indices)) + "\033[0m")
print("Maximum path sum (dynamic programming approach):" + "\033[31m" + str(max_sum) + "\033[0m")
