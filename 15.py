"""

Combinations and NE Lattice Paths

NE lattice paths have close connections to the number of combinations, which are counted by the binomial coefficient, and arranged in Pascal's triangle. The diagram below demonstrates some of these connections.

The number of lattice paths from (0, 0) to (2, 3) is equal to:

    (2 + 3) choose 2 = (5 choose 2) = 10.

The number of lattice paths from (0, 0) to (n, k) is equal to the binomial coefficient (n + k choose n). The diagram shows this for 0 ≤ k ≤ n = 4. If one rotates the diagram 135° clockwise about the origin and extends it to include all n, k ∈ ℕ ∪ {0}, one obtains Pascal's triangle. This result is no surprise, because the kth entry of the nth row of Pascal's Triangle is the binomial coefficient (n choose k).

Source: https://en.wikipedia.org/wiki/Lattice_path

"""

import math

def lattice_paths(grid_size):
    return math.comb(2 * grid_size, grid_size)

# For a 20x20 grid
result = lattice_paths(20)
print("Number of paths through a 20x20 grid:", result)


