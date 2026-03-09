'''for i in range(1,11):
    if i == 5:
        break
    print(i,end=" ")
'''

password = "pavan123"

for i in range(3):
    a = input("enter password: ")
    if password == a:
        print("correct password")
        break
else:
    print("password incorrect")
