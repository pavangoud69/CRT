def add(x,y):
    print(x+y)
def sub(x,y):
    print(x-y)
def mul(x,y):
    print(x*y)
def div(x,y):
    print(x/y)
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
operation = input("Enter the operation you want to perform (+, -, *, /): ")
if operation == "+":
    add(x,y)
elif operation == "-":
    sub(x,y)
elif operation == "*":
    mul(x,y)
elif operation == "/":
    div(x,y)
else:                   
    print("Invalid operation")

