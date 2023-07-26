#loop and dictionary comprehension

students = ['Sam', 'Alice', 'Mona']
subjects = ['Commerce', 'Science', 'Computer']

# Using For Loops
student_subjects = {}
for i in range(len(students)):
    student_subjects[students[i]] = subjects[i]

print(student_subjects)

# Using Dictionary Comprehension
student_subject_dict = {students[i]: subjects[i] for i in range(len(students))}

print(student_subject_dict)
