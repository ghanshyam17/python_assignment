# Input:['Red', 'Blue', 'Black', 'White', 'Pink']
# Output: [['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i','n', 'k']]

def string_to_list_of_chars(s):
    return list(s)

input_list = ['Red', 'Blue', 'Black', 'White', 'Pink']
output_list = list(map(string_to_list_of_chars, input_list))

print("Output:")
print(output_list)
