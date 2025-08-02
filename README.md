---
# Python Scripting Tasks

This repository contains Python scripts that demonstrate basic operations with dictionaries and lists.

## Task 1: Dictionary Lookup for Student Marks

### Problem Statement:

Create a Python program that:

1. Creates a dictionary where student names are keys and their marks are values.
2. Asks the user to input a student's name.
3. Retrieves and displays the corresponding marks.
4. If the student’s name is not found, display an appropriate message.

### Solution:

```python
# Create a dictionary with student names and marks
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 88
}

# Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Retrieve and display the corresponding marks or show an error message
if student_name in students:
    print(f"{student_name}'s marks: {students[student_name]}")
else:
    print(f"{student_name} not found in the database.")
```

### Explanation:

1. A dictionary is created with predefined student names as keys and marks as values.
2. The program asks the user to input a student's name.
3. The program checks if the name exists in the dictionary and prints the corresponding marks or an error message if not found.

---

## Task 2: List Slicing

### Problem Statement:

Write a Python program that:

1. Creates a list of numbers from 1 to 10.
2. Extracts the first five elements from the list.
3. Reverses these extracted elements.
4. Prints both the extracted list and the reversed list.

### Solution:

```python
# Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Extract the first five elements
first_five = numbers[:5]

# Reverse the extracted elements
reversed_five = first_five[::-1]

# Print both the extracted list and the reversed list
print("First five elements:", first_five)
print("Reversed list:", reversed_five)
```

### Explanation:

1. A list of numbers from 1 to 10 is created using `range()`.
2. The first five elements are sliced using `numbers[:5]`.
3. The extracted elements are reversed using list slicing (`[::-1]`).
4. Both the original extracted list and the reversed list are printed.

---

## Requirements

* Python 3.x

---

## How to Run:

1. Save each task in its own `.py` file (e.g., `task1.py`, `task2.py`).
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is saved.
4. Run the program by typing:

   ```bash
   python task1.py  # For Task 1
   python task2.py  # For Task 2
   ```

--
