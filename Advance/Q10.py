def find_walked_away_customers(N, S):
    stack = []
    walked_away_customers = 0

    for customer in S:
        if customer not in stack:
            stack.append(customer)
        else:
            stack.remove(customer)
            walked_away_customers += 1

    return walked_away_customers

# Given Input:
N = 3
S = "GACCBDDBAGEE"

result = find_walked_away_customers(N, S)
print(result)  # Output will be the number of customers who walked away without using a computer
