# If a number is divisible by 3 it should print “Consultadd” as astring
# If a number is divisible by 5 it should print “Python Training” asa string
# If a number is divisible by both 3 and 5 it should print“Consultadd - Python Training” as a string.

def divisible_by_3_and_5(number):
    if number % 3 == 0 and number % 5 == 0:
        return "Consultadd - Python Training"
    elif number % 3 == 0:
        return "Consultadd"
    elif number % 5 == 0:
        return "Python Training"
    else:
        return str(number)

for number in range(1, 21):
    print(divisible_by_3_and_5(number))
