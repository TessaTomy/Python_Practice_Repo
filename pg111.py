# sum of of odd digits in a given number
num=int(input("Enter a number: "))
total=0
for i in str(num):
    if int(i)%2:
        total+=int(i)
print("Sum of odd digits: ",total)