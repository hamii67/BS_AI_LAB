# ===== LAB 1 =====

# PART 1 — Variables
name, age, city = "Imad", 19, "Peshawar"
print(name, age, city)

num1, num2 = 10, 5
print("Sum:", num1+num2)
print("Sub:", num1-num2)
print("Mul:", num1*num2)

# PART 2 — Input Output
n = input("Name: ")
a = input("Age: ")
print(f"Hello {n}, you are {a} years old")

x = int(input("Num1: "))
y = int(input("Num2: "))
print("Add:", x+y, "Sub:", x-y)

# PART 3 — Comments
# Simple python lab
# practicing basics
# learning programming

"""This program shows variables, input,
conditions and loops"""

# PART 4 — Type Check
i, f, s, b = 5, 2.5, "AI", True
print(type(i), type(f), type(s), type(b))

# PART 5 — Data Type
age = int(input("Age: "))
print("After 10 years:", age+10)

m1 = float(input("Marks1: "))
m2 = float(input("Marks2: "))
print("Average:", (m1+m2)/2)

# CONDITIONS
n = int(input("Number: "))
print("Even" if n%2==0 else "Odd")

marks = int(input("Marks: "))
if marks>=80: print("A")
elif marks>=60: print("B")
elif marks>=50: print("C")
else: print("Fail")

age = int(input("Voting age: "))
print("You can vote" if age>=18 else "Not eligible")

# LOOPS
for i in range(1,11): print(i)

t = int(input("Table number: "))
for i in range(1,11):
    print(t,"x",i,"=",t*i)

print("Sum 1–10:", sum(range(1,11)))

# Password Checker
p=""
while p!="admin1234":
    p=input("Enter password: ")
print("Correct")

# FUNCTION
def average(a,b,c):
    return (a+b+c)/3

print("Average:", average(10,20,30))