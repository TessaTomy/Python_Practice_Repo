# print factors common to two numbers

import math
n,m= map(int,input("Enter two numbers: ").split())
gcd=math.gcd(n,m)
print("Common factors of the two numbers: ",end="")
for i in range(1,gcd+1):
    if gcd%i==0:
        print(i,end=" ")