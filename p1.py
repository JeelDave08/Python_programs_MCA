#1. Write a program to input p, r, n and find out interest using simple input output statement.

p = float(input("Enter the principal amount (P):"))
r = float(input("Enter the Rate of interst  (r):"))
n = float(input("Enter the number of years(n):"))
#calculation section
interest =(p*r*n)/100

print("\n --- Result---")
print(f" principal: ",p)
print(f" Rate :", r)
print(f" years:",n)
print(f" The simple Inerest is: {interest}")

