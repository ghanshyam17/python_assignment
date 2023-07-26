# We are making n stone piles! The first pile has n stones.
# If n is even, then all piles have an even number of stones.
# If n is odd, all piles have an odd number of stones. Each pile must have more stones than the previous pile but as few as possible.
# find the number of stones in each pile.

def find_stones_in_piles(n):
    if n % 2 == 0:
        # Even case
        stones_in_a_single_pile = [i for i in range(2, n + 1, 2)]
    else:
        # Odd case
        stones_in_a_single_pile = [i for i in range(1, n, 2)]

    return stones_in_a_single_pile

# Test
n = 7
stones = find_stones_in_piles(n)
print("Stones in a single pile =", stones)
