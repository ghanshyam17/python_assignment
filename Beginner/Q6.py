# Write a Python program to check if a given number is a perfect number.
# A Perfect number is a positive integer that is equal to the sum of its proper divisors. For instance, 6 has divisors 1, 2, and 3, and 1 + 2 +3 = 6, so 6 is a perfect number.
# Input: 5
# Output: No
def is_perfect_number(num):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum == num

# Get input from the user
number = int(input("Enter a number: "))

# Check if the number is a perfect number using the is_perfect_number function
if is_perfect_number(number):
    print(f"{number} is a Perfect number.")
else:
    print(f"{number} is NOT a Perfect number.")
