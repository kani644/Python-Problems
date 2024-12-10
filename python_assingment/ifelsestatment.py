a = 33
b = 200
if b > a:
  print("b is greater than a")


a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

# leap year sum
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# Simple Calculator 
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    print(f"Result: {a + b}")
elif operation == "-":
    print(f"Result: {a - b}")
elif operation == "*":
    print(f"Result: {a * b}")
elif operation == "/":
    if b != 0:
        print(f"Result: {a / b}")
    else:
        print("Division by zero is not allowed")
else:
    print("Invalid operation")