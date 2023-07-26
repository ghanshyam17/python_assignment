# check if a number is a power of two using recursion.
def is_power_of_two(num):
    if num == 1:
        return True
    elif num % 2 != 0 or num == 0:
        return False
    else:
        return is_power_of_two(num // 2)

# Test
num = 16
if is_power_of_two(num):
    print(f"{num} is a power of two.")
else:
    print(f"{num} is not a power of two.")
