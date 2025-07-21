num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

Addition = num1 + num2
Subtraction = num1 - num2
Multiplication = num1 * num2

print("Enter The First Number:", num1)
print("Enter The Second Number:", num2)

print("Addition", Addition)
print("Subtraction:", Subtraction)
print("Multiplication:", Multiplication)
if num2 != 0:
    print(f"Division: {num1 / num2}")
else:
    print("Cannot divide by zero.")

