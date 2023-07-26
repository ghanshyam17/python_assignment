def run_length_encoding(input_string):
    encoded_string = ""
    count = 1

    for i in range(1, len(input_string)):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            encoded_string += input_string[i - 1] + str(count)
            count = 1

    # Add the last character and its count to the encoded string
    encoded_string += input_string[-1] + str(count)

    return encoded_string

# Example usage:
input_str = "wwwwaaadebbbbbw"
encoded_str = run_length_encoding(input_str)
print(encoded_str)
