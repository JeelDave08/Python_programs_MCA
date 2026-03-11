#Write a program to generate arithmetic exception and log the exception in system.

import logging

# Create log file
logging.basicConfig(filename="system.log", level=logging.ERROR)

try:
    a = 10
    b = 0
    c = a / b   # Arithmetic Exception (division by zero)
except ZeroDivisionError as e:
    print("Error occurred")
    logging.error("Arithmetic Exception: %s", e)
