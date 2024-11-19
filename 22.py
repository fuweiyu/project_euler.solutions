# Step 1: Load the file content
with open('0022_names.txt', 'r') as file:
    # Read and split the names by commas, removing the quotes
    names = file.read().replace('"', '').split(',')

# Step 2: Sort the names alphabetically
names.sort()

# Step 3: Define a function to calculate the alphabetical value of a name
def calculate_name_value(name):
    return sum(ord(char) - ord('A') + 1 for char in name)

# Step 4: Compute the total name scores
total_score = 0
for index, name in enumerate(names, start=1):  # Enumerate with position starting at 1
    name_value = calculate_name_value(name)
    total_score += name_value * index

print(f"Total of all name scores in the file: {total_score}")
#Minimal changes
