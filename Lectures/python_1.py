print("AI/ML Batch")

'''
for i in range(1, 11):
    print(7,"x",i," = ", 7*i)
'''
# Data Types
'''
This is a multi line comment
'''
'''
name = "Shradha"
age = 35
PI = 3.14
isFollow = True
print(name," ", age," ", PI, isFollow)
print(type(name)," ", type(age)," ", type(PI), type(isFollow))

# Style Guide --> We follow snake_case in Python
tot_price = 200 # Snake Case
totPrice = 300 # Camel Case
TotPrice = 400 # Pascal Case

# Arithmetic Operators  +, -, *, /, %, **
a = 10
b = 5
print(a+b," ", a-b," ", a*b," ", a/b," ", a%b," ", a**b)

# Relational/Comparison Operators  >, >=, <, <=, ==, !=  Returns True/False
print(a>b," ", a>=b," ", a<b," ", a<=b," ", a==b," ", a!=b)

# Assignment Opeartors  =
a = 5
print(a,end=" ")
a+=1
print(a)

# Logical Operators  not, and, or
var = False
print((not var)," ", (var and True)," ", (var or True))

# Type Conversion
a = int(4.5)
print(a, end=" ")
b = 5 + 10.2
print(b, int(b))

# User Input
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print("Sum is:",a+b)

# Average of 2 number
print((a+b)/2)

# Conditional Statements
age = int(input("Enter your age: "))
if age >= 18:
    print("Yo can cast Vote")
else:
    print("You are not eligible to vote. You can vote after:",int(18-age),"years")

num = int(input("Enter a number: "))
if num%2==0:
    print("Even number")
else:
    print("Odd number")

# Factorial of a number
fact = int(input("Enter a number: "))
f, sum = 1, 0
for i in range(1, fact+1):
    f *= i
    sum += i
print("Factorial of",fact,"is:",f)
print("Sum upto", fact,"is:",sum)

# Match Case
color = input("Enter a color: ")
match color:
    case "Green":
        print("Go")
    case "Yellow":
        print("Look")
    case "Red":
        print("Stop")
    case _:
        print("Wrong color!")
'''

# Loops
cnt = 1
while cnt <= 5:
    print(cnt, ") Hello World", sep="")
    cnt += 1

cnt = 1
while cnt <= 30:
    if (cnt%3 == 0):
        cnt += 1
        continue
    elif (cnt == 28):
        break
    print(cnt, end=" ")
    cnt += 1
print()

cnt = 0
name = "Madiha Mokhtar"
for i in name:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or
        i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        cnt += 1
print("Number of vowels in", name, "is: ",cnt)

# Function
def fibb(fac):
    f = 1
    for i in range(1, fac+1):
        f *= i
    return f
def sum(nm):
    result = 0
    for i in range(nm+1):
        result += i
    return result

nm = int(input("Enter a number: "))
print("Fibonacci & sum of the number", nm, "is:", fibb(nm), "&", sum(nm))
sumToN = lambda a: (a*(a+1))/2
print("Sum of", nm, "using lambda function:", int(sumToN(nm)))
