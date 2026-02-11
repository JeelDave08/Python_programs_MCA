#Write a program to enter 10 numbers and display all armstrong numbers from those numbers.

# Armstrong number program in Python

for i in range(10):
    n = int(input("Enter number: "))
    s = 0
    t = n

    while t > 0:
        d = t % 10
        s = s + d*d*d
        t = t // 10

    if s == n:
        print(n, "is an Armstrong number")
