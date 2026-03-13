#11.Write a program to create function which shall accept any number

def total_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Total =", total)

# calling the function
total_numbers(10, 20, 30)
total_numbers(5, 15, 25, 35)
