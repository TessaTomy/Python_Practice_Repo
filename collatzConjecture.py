# Question: Given a positive integer n, count the number of steps required 
# to reduce it to 1. If n is even, divide it by 2. If n is odd, multiply 
# it by 3 and add 1. Repeat this process until n becomes 1.

def count_steps(n):
    if n == 1:
        return 0
        
    for step in range(1, 10000):
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
            
        if n == 1:
            return step

number = int(input("Enter a number: "))
print(f"Steps: {count_steps(number)}")
