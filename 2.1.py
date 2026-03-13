# Program to demonstrate basic exception handling in Python

try:
    # Taking input from user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    # Performing division
    result = num1 / num2
    
    print("Result:", result)

# Handling division by zero error
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Handling invalid input error
except ValueError:
    print("Error: Please enter valid integers.")

# Executes if no exception occurs
else:
    print("Division performed successfully.")

# Executes whether exception occurs or not
finally:
    print("Program execution completed.")
