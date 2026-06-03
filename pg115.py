#check if first digit of a number odd

num=int(input("Enter a number: "))
temp=num
while temp>=10:
    temp//=10
if temp%2:
    print("The first digit of the number is odd")
else:
    print("The first digit of the number is even")