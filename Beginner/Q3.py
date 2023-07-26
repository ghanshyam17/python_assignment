# Write a Python program to input marks for five subjects Physics,Chemistry, Biology, Mathematics, and Computer. Calculate thepercentage and grade according
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F

def calculate_percentage(total_marks, obtained_marks):
    return (obtained_marks / total_marks) * 100

def calculate_grade(percentage):
    if percentage >= 90:
        return "Grade A"
    elif percentage >= 80:
        return "Grade B"
    elif percentage >= 70:
        return "Grade C"
    elif percentage >= 60:
        return "Grade D"
    elif percentage >= 40:
        return "Grade E"
    else:
        return "Grade F"

# Get input marks from the user for each subject
physics_marks = float(input("Enter Physics marks: "))
chemistry_marks = float(input("Enter Chemistry marks: "))
biology_marks = float(input("Enter Biology marks: "))
mathematics_marks = float(input("Enter Mathematics marks: "))
computer_marks = float(input("Enter Computer marks: "))

# Calculate total marks (assuming maximum marks for each subject is 100)
total_marks = 500
obtained_marks = physics_marks + chemistry_marks + biology_marks + mathematics_marks + computer_marks

# Calculate the percentage
percentage = calculate_percentage(total_marks, obtained_marks)

# Calculate the grade
grade = calculate_grade(percentage)

# Print the output
print(f"Percentage: {percentage:.2f}% | Grade: {grade}")

