# find product of even digits in a given number

num=int(input("Enter a number: "))
product=1
while num:
    digit=num%10
    if not digit%2:
        product*=digit
    num//=10
print("Product of even digits: ",product)