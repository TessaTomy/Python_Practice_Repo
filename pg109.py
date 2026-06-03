# find smallest digit and its frequency in a given number
num=int(input("Enter a number: "))
smallest=9
count=0
for i in str(num):
    if int(i)<smallest:
        smallest=int(i)
        count=1
    elif int(i)==smallest:
        count+=1
print("Smallest digit: ",smallest)
print("Frequency of smallest digit: ",count)