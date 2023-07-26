# Input: l1 = [1, 2, 3, 4, 5] and l2 = [4, 5, 6, 7, 8]
# output: [4, 5]

def find_common_elements(l1, l2):
    return list(set(l1) & set(l2))

l1 = [1, 2, 3, 4, 5]
l2 = [4, 5, 6, 7, 8]
common_elements = find_common_elements(l1, l2)
print(common_elements)




