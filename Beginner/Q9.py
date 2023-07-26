# Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
# Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}

def count_frequency(input_list):
    frequency_count = {}
    for element in input_list:
        if element in frequency_count:
            frequency_count[element] += 1
        else:
            frequency_count[element] = 1
    return frequency_count

# Input list
input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]

# Call the function to count the frequency of each element
result = count_frequency(input_list)

# Print the output
print("Frequency count:", result)
