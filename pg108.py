# find largest digit and its frequency in a given number
num=int(input("Enter a number: "))
largest=0
count=0
for i in str(num):
    if int(i)>largest:
        largest=int(i)
        count=1
    elif int(i)==largest:
        count+=1
print("Largest digit: ",largest)
print("Frequency of largest digit: ",count)