# count common factors of two numbers

import math
n,m= map(int,input("Enter two numbers: ").split())
gcd=math.gcd(n,m)
count=0
for i in range(1,gcd+1):
    if gcd%i==0:
        count+=1
print("Common factors of the two numbers: ",count)