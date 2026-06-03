#find sum of prime numbers from 1 to n

def prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    if prime(i):
        sum+=i
print("The sum of prime numbers from 1 to",n,"is",sum)