# count palindrome numbers in a given range

n,m= map(int,input("Enter the range: ").split())
count=0
for i in range(n,m+1):
    if str(i)==str(i)[::-1]:
        count+=1
print("Palindrome numbers in the given range: ",count)