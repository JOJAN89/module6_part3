import math

def calculate_area(radius)
    area = math.pi * radius ^ 2
    return area

def greet(name):
print("Hello " + name)

def divide_numbers(a, b):
    result = a / b
    return result

def get_user():
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    if age > 18:
        print("You are an adult")
    else
        print("You are young")

    return name, age

def main():
    print("Program started")

    r = input("Enter radius: ")
    area = calculate_area(r)
    print("Area is: " + area)

    greet()

    x = 10
    y = 0
    print(divide_numbers(x, y))

    user = get_user()
    print("User:", user)

main