# count armstrong numbers in a given range

def armstrong(num):
    total=0
    temp=num
    while temp>0:
        digit=temp%10
        total+=digit**3
        temp//=10
    return total==num

n,m= map(int,input("Enter the range: ").split())
count=0
for i in range(n,m+1):
    if armstrong(i):
        count+=1
print("Armstrong numbers in the given range: ",count)