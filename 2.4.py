#Create a module with 4 functions of your choice. Import and use the functions using module in different ways.

# mymodule.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def greet(name):
    return "Hello " + name

# 1. Normal function call
print("Normal function call:")
print(add(5, 3))
print(greet("Sam"))

# 2. Using alias name
addition = add
print("\nUsing alias name:")
print(addition(10, 5))

# 3. Storing functions in a list (like import *)
functions = [subtract, multiply]
print("\nUsing functions from list:")
print(functions[0](10, 4))   # subtract
print(functions[1](3, 6))    # multiply)

# 4. Calling inside main block
if __name__ == "__main__":
    print("\nInside main block:")
    print(greet("Alex"))
