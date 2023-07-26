# Input: arr = [1, 2, 3, 4, 5], k = 6
# Output: Pair count: 2

def count_pairs_with_sum(arr, k):
    count = 0
    seen = set()

    for num in arr:
        complement = k - num
        if complement in seen:
            count += 1
        seen.add(num)

    return count

arr = [1, 2, 3, 4, 5]
k = 6
pair_count = count_pairs_with_sum(arr, k)
print("Pair count:", pair_count)
