# find the sum of the factorials from 1 to n

n=int(input("Enter a number: "))
fact=1
sum=0
for i in range(1,n+1):
    fact=fact*i
    sum+=fact
print("The sum of the factorials from 1 to",n,"is",sum)