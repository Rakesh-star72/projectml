# Simple Calculator Program

# Take first number input
num1 = float(input("Enter first number: "))

# Take operator input
operator = input("Enter operator (+, -, *, /): ")

# Take second number input
num2 = float(input("Enter second number: "))

# Perform calculation
if operator == "+":
    result = num1 + num2
    print("Result:", result)

elif operator == "-":
    result = num1 - num2
    print("Result:", result)

elif operator == "*":
    result = num1 * num2
    print("Result:", result)

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid operator!")