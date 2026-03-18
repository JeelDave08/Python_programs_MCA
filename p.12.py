#12.Write a program to display the use of local, global and nonlocal variables

x = 10   # Global variable

def outer():
    y = 20   # Enclosing (nonlocal) variable

    def inner():
        global x
        nonlocal y

        x = x + 5
        y = y + 5
        z = 30   # Local variable

        print("Inside inner function:")
        print("Global x =", x)
        print("Nonlocal y =", y)
        print("Local z =", z)

    inner()
    print("Inside outer function, y =", y)

outer()
print("Outside function, x =", x)
