'''
Bug -->error
Finding and Fixing of error is called Debugging 
#Types
1,syntax erroe: missing colon, indentation mistake
2,run time error: division of my num with zero
3,logical error: missing of logics

Debugging Techniques: 
1,print()
2,try-except
3,Using of pdb

'''
'''
a = int(input("Enter a"))
b = int(input("Enter a"))
c = a+b
print("value a is:", a)
print("value a is:", b)
print("Sum a is:", c)
'''
'''
try:
    a = int(input("Enter a: "))
    print(10/a)
except ZeroDivisionError:
    print("Can not be divisible by zero")
except ValueError:
    print("Invalid input")
'''
'''
# pdb-->python debugger
# purpose:
          1, pause the execution
          2,inspect the variable's value
          3,to run the code step by step

          pdb commands:
          1.n --> to get output in next line
          2.p variable --> to get the value of that variable
          3.l --> list nearby code
          4.c --> continue the execution 
          5.s --> start the function
          6.r --> to return from the function 
          7.h --> help
          8.q --> quit the execution
'''
import pdb

def add(a,b):
    pdb.set_trace() 
    return a+b
a = int(input("Enter a"))
b = int(input("Enter b"))
print(add(a,b))

