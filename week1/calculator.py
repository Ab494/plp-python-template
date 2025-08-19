# Simple calculator 
# Get input from user 

num1 = float(input("Enter first number: "))

# promt the user to enter the operator
operator = input("Enter operation (+, -, *, /): ")

# promt the user to enter the second number
num2 = float(input("Enter second number: "))

# perform operation

if operator == '+':
    result = num1 + num2 
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero" 
else:
    result = "Invalid operator"

# display results
print(f"{num1} {operator} {num2} = {result}")   
# End of calculator.py