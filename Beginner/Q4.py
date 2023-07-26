# Start = 1, stop = 10
# Sum of odd numbers: 25
def sum_odd_numbers(start, stop):
    total_sum = 0
    for number in range(start, stop + 1):
        if number % 2 != 0:
            total_sum += number
    return total_sum

# Get input from the user for start and stop values
start = int(input("Enter the start number: "))
stop = int(input("Enter the stop number: "))

# Call the function to calculate the sum of odd numbers
result = sum_odd_numbers(start, stop)

# Print the output
print(f"Sum of odd numbers between {start} and {stop}: {result}")
