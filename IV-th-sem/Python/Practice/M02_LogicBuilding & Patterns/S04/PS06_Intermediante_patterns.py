'''li = [1,2,3,4,5]
res=[]
for i in li:
    res.append(i*2)    
print(res)
li = [1,2,3,4,5]
print([i for i in li if i % 2 == 0])
'''
'''#['a', 'b', 'c'] => ["abc"]
li = ['a', 'b', 'c']
print(["".join(li)])'''
"""
output:
   *
  * * 
 * * *
* * * *
"""
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
'''
output:
* * * *
 * * *
  * *
   *
'''
n = int(input("Enter the number of rows: "))
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)
"""
output:
   *
  * *
 * * *
* * * *
 * * *
  * *
   *
"""
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)
"""
   1
  1 2
 1 2 3 
1 2 3 4
"""
n = int(input("Enter the number of rows: "))    
for i in range(1, n + 1):
    print(" " * (n - i) + " ".join(str(x) for x in range(1, i + 1)))
'''
A
B C
D E F
G H I J
'''    
n = int(input("Enter the number of rows: "))
val = 65
for i in range(n):
    for j in range(i+1):
        print(chr(val),end=" ")
        val += 1
    print()

    