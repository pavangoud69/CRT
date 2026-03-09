'''
n = int(input("Enter a number: "))
factors = []
for i in range(1, n+1): 
    if n % i == 0:
        factors.append(i)

print("Factors of", n, "are:", factors)


start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
if start == 1:
    start = 2
for n in range(start,end+1):
    counter = 0
    for i in range(2,n//2+1):
        if n % i == 0:
            counter += 1
    if counter == 0:
        print(n, end=" ")


n = int(input("Enter a number: "))
if n <0:
    print("Negative numbers are not prime.")
elif n == 0 or n == 1:
    print(1)
else:
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)        

#gcd of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
while b:    
    a, b = b, a % b
print(a)


import math
print(math.gcd(a,b))
n = int(input("Enter a number: "))
#using list
fib = [0,1]
for i in range(2,n):
    fib.append(fib[i-1] + fib[i-2])
for i in fib:
    print(i, end=" ")    
'''

