#check if a number ends with an even digit
num=int(input("Enter a number: "))
if not num%10%2:
    print("The number ends with an even digit")
else:
    print("The number ends with an odd digit")