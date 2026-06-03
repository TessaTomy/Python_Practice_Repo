#find the product of odd numbers from 1 to n

n=int(input("Enter a number: "))
product=1
for i in range(1,n+1,2):
    product=product*i
print("The product of odd numbers from 1 to",n,"is",product)