# calculate the sum of digits of a given number until the sum becomes a single-digit number.
# Sample Input: num = 987
# Sample Output: Sum_of_digits = 24,
# Again compute the sum of digits so that it can be reduced to
# on single digit.
# Final Output: 6

def sum_of_digits(number):
    while number > 9:
        digit_sum = 0
        while number > 0:
            digit_sum += number % 10
            number //= 10
        number = digit_sum
    return number

# Sample Input
num = 987

# Calculate the sum of digits
sum_of_digits_result = sum_of_digits(num)

# Print the intermediate sum of digits
print("Sum_of_digits:", sum_of_digits_result)

# Compute the sum of digits again until it becomes a single-digit number
final_output = sum_of_digits(sum_of_digits_result)

# Print the final output
print("Final Output:", final_output)
