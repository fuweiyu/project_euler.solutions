def read_triangle(filename):
    with open(filename, 'r') as file:
        triangle = [list(map(int, line.split())) for line in file]
    return triangle

def max_path_sum(triangle):
    # Create a copy of the triangle to calculate the path without modifying the original
    triangle_copy = [row[:] for row in triangle]

    # Start from the second last row and move upwards
    for row in range(len(triangle_copy) - 2, -1, -1):
        for col in range(len(triangle_copy[row])):
            # Update the current element with the maximum path sum from below
            if triangle_copy[row + 1][col] > triangle_copy[row + 1][col + 1]:
                triangle_copy[row][col] += triangle_copy[row + 1][col]
            else:
                triangle_copy[row][col] += triangle_copy[row + 1][col + 1]
    
    # The top element will contain the maximum path sum
    max_sum = triangle_copy[0][0]
    
    # Track the path from the top to bottom based on the computed sums
    index = 0
    path_indices = [index]
    for row in range(1, len(triangle_copy)):
        if index + 1 < len(triangle_copy[row]) and triangle_copy[row][index + 1] > triangle_copy[row][index]:
            index += 1
        path_indices.append(index)

    return max_sum, path_indices

# Read the triangle from the file
triangle = read_triangle('0067_triangle.txt')

# Find the maximum path sum and path indices
max_sum, path_indices = max_path_sum(triangle)

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

# Print the path indices and maximum path sum
print("\033[31m" + str(path_indices) + "\033[0m")
print("Maximum path sum (dynamic programming approach):" + "\033[31m" + str(max_sum) + "\033[0m")
