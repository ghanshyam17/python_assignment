# Input: temperature_readings = [25, 28, 21, 24, 27]
# Output:
# Average Temperature: 25.0
# Highest Temperature: 28
# Lowest Temperature: 21

def analyze_temperature_data(temperature_readings):
    average_temperature = sum(temperature_readings) / len(temperature_readings)
    highest_temperature = max(temperature_readings)
    lowest_temperature = min(temperature_readings)

    return average_temperature, highest_temperature, lowest_temperature

temperature_readings = [25, 28, 21, 24, 27]
avg_temp, highest_temp, lowest_temp = analyze_temperature_data(temperature_readings)
print("Average Temperature:", avg_temp)
print("Highest Temperature:", highest_temp)
print("Lowest Temperature:", lowest_temp)


