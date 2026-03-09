'''user = int(input("Enter a number: "))
print(len(user))
'''
'''
n = int(input("Enter a number: "))
count = 0
while n > 0:
    n = n // 10
    count += 1
print(count)
print(len(str(n)))
'''
'''
n = int(input("Enter a number: "))
temp=n
s =0 
while n > 0:
    s+=(n%10)
    n = n//10
print(s)
print(sum(map(int, str(temp))))
'''
'''
n = int(input("number: "))
even = odd = 0
while n > 0:
    if(n%2) == 0:
        even += 1
    else:
        odd += 1
    n //=10
print(even,odd)'''
'''
n = int(input("number: "))
while n >9:
    n = sum(map(int, str(n)))
print(n)

'''
n= int(input("number: "))
m= int(input("number: "))
if n > m:
    print("n is greater than m")
elif n < m:
    print("m is greater than n")