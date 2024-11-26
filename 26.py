def find_longest_recurring_cycle(limit):
    max_length = 0
    result = 0

    for d in range(2, limit):
        remainders = {}
        value = 1
        position = 0

        while value != 0 and value not in remainders:
            remainders[value] = position
            value = (value * 10) % d
            position += 1

        if value != 0:  # Recurring cycle found
            cycle_length = position - remainders[value]
            if cycle_length > max_length:
                max_length = cycle_length
                result = d

    return result, max_length


# Find the value of d < 1000 with the longest recurring cycle
d, cycle_length = find_longest_recurring_cycle(1000)
print(f"The value of d < 1000 with the longest recurring cycle is {d}, with a cycle length of {cycle_length}.")
