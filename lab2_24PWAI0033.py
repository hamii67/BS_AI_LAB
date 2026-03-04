# TASK 01

name = input("Enter your full name: ")
color = input("Enter your favorite color: ")
birth_year = int(input("Enter your birth year: "))

age = 2026 - birth_year

print(f"Welcome, {name}!")
print(f"Your favorite color is {color}.")
print(f"You are {age} years old.")


# TASK 02

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+ - * / ** %): ")

if op == "+":
    print(f"{num1} + {num2} = {num1 + num2}")

elif op == "-":
    print(f"{num1} - {num2} = {num1 - num2}")

elif op == "*":
    print(f"{num1} * {num2} = {num1 * num2}")

elif op == "/":
    if num2 == 0:
        print("Cannot divide by zero!")
    else:
        print(f"{num1} / {num2} = {num1 / num2:.2f}")

elif op == "**":
    print(f"{num1} ** {num2} = {num1 ** num2:.2f}")

elif op == "%":
    print(f"{num1} % {num2} = {num1 % num2}")

else:
    print("Invalid operator!")


# TASK 03 - Challenge A

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

while start <= end:

    if start % 7 == 0:
        start += 1
        continue

    if start % 2 == 0 and start % 5 == 0:
        print("Even & Multiple of 5")
    elif start % 2 == 0:
        print("Even")
    elif start % 5 == 0:
        print("Multiple of 5")
    else:
        print("Odd")

    start += 1


# Challenge B

password = input("Enter password: ")

if len(password) < 6:
    print("Too short!")

elif not any(char.isdigit() for char in password):
    print("Add at least one number")

elif not any(char.isupper() for char in password):
    print("Add at least one capital letter")

else:
    print("Strong password")