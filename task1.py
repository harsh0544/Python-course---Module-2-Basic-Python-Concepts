students = {
    "harsh": 85,
    "rohit": 92,
    "shivam": 78,
    "prachi": 88
}

student_name = input("Enter the student's name: ")

if student_name in students:
    print(f"{student_name}'s marks: {students[student_name]}")
else:
    print(f"{student_name} not found in the database.")
