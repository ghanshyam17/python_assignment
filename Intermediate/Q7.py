# print the median of a list of numbers.
# Sample Input: number_list = [7, 2, 5, 1, 9, 3]
# Sample Output: Median: 4.0

def find_median(number_list):
    sorted_list = sorted(number_list)
    n = len(sorted_list)

    if n % 2 == 0:
        mid = n // 2
        median = (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        mid = n // 2
        median = sorted_list[mid]

    return median

# Test
number_list = [7, 2, 5, 1, 9, 3]
median_value = find_median(number_list)
print("Median:", median_value)
