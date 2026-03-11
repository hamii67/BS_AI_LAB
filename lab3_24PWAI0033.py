# Task 1 – Basic Function and Function Call
def welcome_message():
    print("Welcome to Python Programming Lab")

welcome_message()


# Task 2 – Function with Parameters and Return
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print("Sum =", result)


# Task 3 – Function Call Stack Co
def functionB():
    print("Inside Function B")

def functionA():
    print("Inside Function A")
    functionB()

functionA()


# Task 4 – Default Parameters
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Imad")


# Task 5 – Variable Scope
x = 10   # global variable

def my_function():
    print("Value of x:", x)
    y = 20
    print("Value of y:", y)

my_function()

print("Value of x outside function:", x)




# Task 6 – Variable Length Arguments (*args)
def total_numbers(*numbers):
    total = sum(numbers)
    return total

print("Total =", total_numbers(2,3,4,5))


# Task 7 – Keyword Variable Arguments (**kwargs)
def student_info(**data):
    for key, value in data.items():
        print(key, ":", value)

student_info(name="Imad", age=19, city="Peshawar")


# Task 8 – Lambda Function
square = lambda x: x * x
print("Square =", square(5))


# Task 9 – Lambda with List
numbers = [1,2,3,4,5]
squares = list(map(lambda x: x*x, numbers))
print("Squares:", squares)


# Task 10 – Lambda with Filter
marks = [45, 67, 82, 30, 90, 55]
result = list(filter(lambda x: x > 50, marks))
print("Marks greater than 50:", result)