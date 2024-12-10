# na
def maximumNum(a, b, c):
    if a > b and a > c:     
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)

maximumNum(b=12, a=10, c=3)         

def minmumOfThree(a, b, c):
    if a < b and a < c:
        print(a)
    elif b < a and b < c:
        print(b)    
    else:
        print(c)

minmumOfThree(c=9, a=8, b=12)


for i in range(1, 11):  
    if i % 2 == 0:  
        print(i)

i = 1 
while i <= 10:  
    if i % 2 == 0:  
        print(i)
    i += 1 


largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    print(num)

print("Maximum", largest)

