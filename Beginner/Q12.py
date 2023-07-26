# reverse a number using a while loop.
# Sample Input: num = 12345
# Sample Output: rev num = 54321
def reverse_number(number):
    reversed_num = 0
    while number > 0:
        remainder = number % 10
        reversed_num = reversed_num * 10 + remainder
        number //= 10
    return reversed_num

# Sample Input
num = 12345

# Call the function to reverse the number
revnum = reverse_number(num)

# Print the output
print("Reversed number:", revnum)
