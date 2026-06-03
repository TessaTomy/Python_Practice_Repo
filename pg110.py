# find sum of even digits in a given number
num=int(input("Enter a number: "))
total=0
for i in str(num):
    if not int(i)%2:
        total+=int(i)
print("Sum of even digits: ",total)