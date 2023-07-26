# Write a Python program to find if a given string starts with a given character using Lambda.
# input: input_string = "Hello, World!", given_char = "H"
# Output: True

check_start_with_char = lambda input_string, given_char: input_string.startswith(given_char)

input_string = "Hello, World!"
given_char = "H"

result = check_start_with_char(input_string, given_char)
print(result)
