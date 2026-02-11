#2. Write a program to input 2 numbers and one arithmetic operator. Perform operations as per arithmetic operator which is given as input

a = int (input("Enter first number"))
b = int (input("Enter second number"))
op = input ("Enteroperator (+ - * /):")

if op =='+':
     print("Result+", a+b)
elif op == '-':
      print("Result-", a-b)
elif op == '*':
      print("Result*", a*b)
elif op == '/':
      print("Result/", a/b)
else:
    print("invalid operator")
          
