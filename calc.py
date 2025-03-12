# Function to perform the desired mathematical operation
def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        return None

# Ask the user to input two numbers and an operation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation and print the result
result = calculate(num1, num2, operation)
if result is not None:
    print(f"{num1} {operation} {num2} = {result}")
else:
    print("Invalid operation entered.")

