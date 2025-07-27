def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

result = factorial(5)
print(f"The factorial of 5 is: {result}")
