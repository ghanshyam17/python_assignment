class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, other_time):
        total_minutes = self.minutes + other_time.minutes
        extra_hours = total_minutes // 60
        minutes_left = total_minutes % 60

        total_hours = self.hours + other_time.hours + extra_hours

        return Time(total_hours, minutes_left)

    def __str__(self):
        return f"{self.hours} hr and {self.minutes} min"

# Example usage:
time1 = Time(2, 50)
time2 = Time(1, 20)

sum_time = time1.addTime(time2)
print(f"({time1}) + ({time2}) is ({sum_time})")
