#Write a program to enter 10 numbers and display largest odd number from the entered number.

# Program to find largest odd number from 10 numbers

largest = None

for i in range(10):
    n = int(input("Enter number: "))

    if n % 2 != 0:
        if largest is None or n > largest:
            largest = n

if largest is not None:
    print("Largest odd number is:", largest)
else:
    print("No odd number entered")
