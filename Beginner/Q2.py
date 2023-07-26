# Input: Hello123
# Output: Alphabets: 5 & Number : 3

def count_letters_and_digits(input_string):
    letters_count = 0
    digits_count = 0

    for char in input_string:
        if char.isalpha():
            letters_count += 1
        elif char.isdigit():
            digits_count += 1

    return letters_count, digits_count

# Get input from the user
user_input = input("Enter a string: ")

# Call the function to count letters and digits
letters, digits = count_letters_and_digits(user_input)

# Print the output
print(f"Alphabets: {letters} & Numbers: {digits}")
