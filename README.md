---
# Python Programs

This repository contains solutions to two Python programming tasks.

## Task 1: Check if a Number is Even or Odd

### **Problem Statement**

Write a Python program that:

1. Takes an integer input from the user.
2. Checks whether the number is even or odd using an if-else statement.
3. Displays the result accordingly.

### **Expected Output**

The program should return an output like:

```
Enter an Nummber: 4
4 is even Number.
```

### **How It Works**

1. The program takes an integer input from the user.
2. It checks if the number is divisible by 2 using the modulus operator (`%`).

   * If the remainder is 0, the number is **even**.
   * Otherwise, the number is **odd**.
3. Based on the result, the program prints whether the number is even or odd.

---

## Task 2: Sum of Integers from 1 to 50 Using a Loop

### **Problem Statement**

Write a Python program that:

1. Uses a `for` loop to iterate over numbers from 1 to 50.
2. Calculates the sum of all integers in this range.
3. Displays the final sum.

### **Expected Output**

The program should return an output like:

```
The sum of Number from 1 to 50 is: 1275
```

### **How It Works**

1. A variable `sum_of_numbers` is initialized to 0 to store the running total.
2. The `for` loop iterates through numbers 1 to 50 (using `range(1, 51)`).
3. In each iteration, the current number is added to `sum_of_numbers`.
4. After the loop finishes, the program prints the final sum, which is the sum of integers from 1 to 50.

---

## How to Run the Programs

### **1. Check if a Number is Even or Odd:**

* Copy the code for **Task 1** into a Python file (e.g., `task1.py`).

* Run the program in the terminal using the command:

  ```bash
  task1.py
  ```

* Enter an integer when prompted, and the program will display whether the number is even or odd.

### **2. Sum of Integers from 1 to 50 Using a Loop:**

* Copy the code for **Task 2** into a Python file (e.g., `task2.py`).

* Run the program in the terminal using the command:

  ```bash
task2.py
```

* The program will automatically calculate and display the sum of integers from 1 to 50.

---

## License

This repository is open-source and available for personal or educational use.

---
