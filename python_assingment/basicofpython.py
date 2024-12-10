# Basic of Python
print("Hello World")

x = 5
y = "John"
print(x)
print(y)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))


x, y, z = "Orange", "Banana", "Cherry"
print(x)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = "awesome"
def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

# string
a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x) 

a = "Hello, World!"
print(len(a)) #length of the string

b = "Hello, World!"
print(b[2:5])

a = "Hello, World!"
b = a.split(",")
print(b)

age = 36
txt = f"My name is John, I am {age}"
print(txt)

a = 10
b = 5

# Addition
print("Addition:", a + b)

# Subtraction
print("Subtraction:", a - b)

# Multiplication
print("Multiplication:", a * b)

# Division
print("Division:", a / b)

# Modulus
print("Modulus (Remainder):", a % b)

# Exponentiation
print("Exponentiation:", a ** b)

# Floor Division
print("Floor Division:", a // b)



id = "rupesh"
domain = "cse.iitm.ac.in"
print(id, domain, sep='@')  

print('Enter your name: kani')
name = input()
print('Enter your year of birth: 2003')
yob = input() 
print ('Enter your name:')
name = input()
print ('Enter your date of birth')

#x = str(3)    # x will be '3'
#y = int(3)    # y will be 3
#z = float(3)  # z will be 3.0

x ="kani"
y= 5


print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")


# print the brand value
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])





# def pyramid_pattern(n):
#     for i in range(1, n + 1):
#         print(" " * (n - i) + "".join(str(j) for j in range(1, i)) + 
#               "".join(str(j) for j in range(i, 0, -1)))

# pyramid_pattern(5)

# def factorial(n):
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(5))


# def gradeCalculator(mark):
#     # 90 and above grade A
#     if mark >= 90:
#         print("A")
#     elif mark >= 80 and mark < 90:
#         print("B")
#     elif mark >= 70 and mark < 80:
#         print ("C")
#     elif mark >=50 and mark < 70:
#         print ("D")
#     else:
#         print("E")

# mark = int(input("Enter your marks:"))
# gradeCalculator(mark)



# x = 5.9
# print(type(x))

# num = "6.0"
# print(type(float(num)))


# def reverse_string(input_string):
#     return input_string[::-1]  

# string = input("Enter a string to reverse: ")
# reversed_string = reverse_string(string)
# print("Reversed String:", reversed_string)

# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2, number):  
#         if number % i == 0:
#             return False
#     return True

# num = int(input("Enter a number: "))


# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")

# def count_vowels(text):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in text:
#         if char in vowels:
#             count += 1
#     return count

# string = input("Enter a string: ")
# vowel_count = count_vowels(string)
# print(f"The number of vowels in the string is: {vowel_count}")

# def is_palindrome(string):
#     cleaned_string = string.replace(" ", "").lower() 
#     return cleaned_string == cleaned_string[::-1]
# input_string = input("Enter a string: ")

# if is_palindrome(input_string):
#     print(f'"{input_string}" is a palindrome!')
# else:
#     print(f'"{input_string}" is not a palindrome.')
  

# cleaned_string = string.replace(" ", "").lower()