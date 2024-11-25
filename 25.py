def find_fibonacci_index_with_digits(digits):
    # Starting with F1 = 1, F2 = 1
    fib1, fib2 = 1, 1
    index = 2  # F2 corresponds to index 2

    while True:
        # Calculate the next Fibonacci number
        fib_next = fib1 + fib2
        index += 1

        # Check if the number has the required digits
        if len(str(fib_next)) >= digits:
            return index

        # Move to the next pair of Fibonacci numbers
        fib1, fib2 = fib2, fib_next


# Find the index of the first Fibonacci number with 1000 digits
result = find_fibonacci_index_with_digits(1000)
print(f"The index of the first Fibonacci number with 1000 digits is {result}.")
