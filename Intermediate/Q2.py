# Input: list1 = [1, 2, 2, 3, 4, 4, 5, 5]
# Output: list2 = [1, 2, 3, 4, 5]

def unique_elements(input_list):
    return list(set(input_list))

list1 = [1, 2, 2, 3, 4, 4, 5, 5]
list2 = unique_elements(list1)
print(list2)
