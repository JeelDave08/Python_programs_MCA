class Number:
    def __init__(self, value):
        self.value = value

    # Overloading + operator
    def __add__(self, other):
        return Number(self.value + other.value)

    # Overloading - operator
    def __sub__(self, other):
        return Number(self.value - other.value)

    def display(self):
        print("Value:", self.value)


# Main Program
n1 = Number(20)
n2 = Number(10)

# Addition
result_add = n1 + n2
print("Addition Result:")
result_add.display()

# Subtraction
result_sub = n1 - n2
print("Subtraction Result:")
result_sub.display()
