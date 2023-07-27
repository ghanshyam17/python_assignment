def find_walked_away_customers(N, S):
    occupied_computers = {}
    customer_worked_on_computer = 0
    walked_away_customers = 0
    walked_away_list = []
    for customer in S:
        if customer not in occupied_computers:
            if len(occupied_computers) < N:
                occupied_computers[customer] = 1
            elif len(occupied_computers) == N:
                walked_away_list.append(customer)

        else:
            occupied_computers[customer] += 1
            if occupied_computers[customer] == 2:
                del occupied_computers[customer]
                customer_worked_on_computer += 1

    return len(set(walked_away_list))

# Given Input:

N1 = 3
S1 = "GACCBDDBAGEE"
N2 = 1
S2 = "ABCBAC"

result1 = find_walked_away_customers(N1, S1)
print(result1)  # Output will be the number of customers who walked away without using a computer

result2 = find_walked_away_customers(N2, S2)
print(result2)  # Output will be the number of customers who walked away without using a computer

