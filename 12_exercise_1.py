# Basic Calculator

num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(f"The result of {num1} + {num2} is {result}")
elif operator == "-":
    result = num1 - num2
    print(f"The result of {num1} - {num2} is {result}")
elif operator == "*":
    result = num1 * num2
    print(f"The result of {num1} * {num2} is {result}")
elif operator == "/":
    if num2 == 0:
        print("Error! Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {result}")
else:
    print("Invalid operator! Please enter one of (+, -, *, /).")
