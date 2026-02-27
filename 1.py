#Write a program to display basic exception handling in python.

try:
    n=0
    res = 100/n
except ZeroDivisionError:
        print("you cant divide by zero")
except Valueerror:
        print("Enter a valid number!")
else:
        print("Result is",res)
finally:
        print("Execution complete")
        
