def count_coin_sums(target, coins):
    """
    Count the number of ways to make the target amount using the given coins.
    """
    # Initialize a list to store the number of ways to make each amount
    ways = [0] * (target + 1)
    ways[0] = 1  # There's one way to make 0 pence: use no coins

    # For each coin, update the ways array
    for coin in coins:
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]

    return ways[target]

# Define the coins in pence
coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200

# Calculate the number of ways to make £2
result = count_coin_sums(target, coins)
print(f"The number of different ways to make £2 is {result}.")
