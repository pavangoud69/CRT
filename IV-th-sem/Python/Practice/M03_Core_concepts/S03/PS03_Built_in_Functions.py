'''
1)Find the largest number (using(max))
2)Check Palindrome (Using reversed() & join())
3)Count Even Numbers (Using(filter()))
4)Remove Duplicates( Using sum())
5)Sum of DIgits (using(sum()))
6) sort words alphabetically (using(sort()))
7)find common elements(using(set()))
8)index with calue (using Enumerate())
9)pair two lists(using zip())
10)find second largest number(using sorted())'''
#Find the largest number (using(max))
a = [10,20,87,15,98,12,3,2,45,100]
print(max(a))

#Check Palindrome (Using reversed() & join())
def is_palindrome(s):
    return s == ''.join(reversed(s))
word = "radar"
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:    print(f"{word} is not a palindrome.")

#Count Even Numbers (Using(filter()))    
a = [10,20,87,15,98,12,3,2,45,100]
res = list(filter(lambda x:x%2 == 0,a))
print(res)
print(len(res))

#Remove Duplicates( Using sum())
a = [10,20,87,15,98,12,3,2,45,100]
print(set(a))

#Sum of DIgits (using(sum()))
n = 12345
res = sum(int(digit) for digit in str(n))
print(res)

#sort words alphabeticcally (using sort())
words = ["banana", "apple", "grape", "orange"]
words.sort()
print(words)

#find common elements(using(set()))
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1) & set(list2))
print(common)

#index with calue (using Enumerate())
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

#pair two lists(using zip())
list1 = [1, 2, 3]       
list2 = ['a', 'b', 'c']
paired = list(zip(list1, list2))
print(paired)

#find second largest number(using sorted())
a = [10,20,87,15,98,12,3,2,45,100]
sorted_a = sorted(a, reverse=True)
second_largest = sorted_a[1]
print(second_largest)
