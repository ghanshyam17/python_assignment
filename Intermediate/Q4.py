# Input: arr = [1, 2, 3, 4, 5], D = 2
# Output: arr after rotation = [4, 5, 1, 2, 3]

def rotate_array(arr, d):
    n = len(arr)
    d = d % n
    return arr[-d:] + arr[:-d]

arr = [1, 2, 3, 4, 5]
D = 2
arr_after_rotation = rotate_array(arr, D)
print("arr after rotation =", arr_after_rotation)
