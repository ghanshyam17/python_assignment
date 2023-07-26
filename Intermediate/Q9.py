# IndexError exception if the index is out of range.

def handle_index_error(input_list, index):
    try:
        result = input_list[index]  # Perform the desired operation on the list
        return result
    except IndexError:
        print("Error: Index out of range.")
        return None

my_list = [1, 2, 3, 4, 5]
index = 10
result = handle_index_error(my_list, index)
if result is not None:
    print("Result:", result)
