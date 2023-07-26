# Write a Python program to find the factorial of a number using a for loop.
def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

# Get input from the user
number = int(input("Enter a number: "))

# Calculate the factorial using the factorial function
factorial_result = factorial(number)

# Print the output
print(f"The factorial of {number} is: {factorial_result}")
