''' 168,169,170
Count prime digits and non-prime digits in a number
Find the largest prime digit in a number
Find the smallest prime digit in a number'''
def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

N = int(input("N: "))

prime_count = 0
non_prime_count = 0
largest_prime = -1
smallest_prime = 10

for digit_char in str(abs(N)):
    digit = int(digit_char)
    
    if is_prime(digit):
        prime_count += 1
        
        
        if digit > largest_prime:
            largest_prime = digit
            
        
        if digit < smallest_prime:
            smallest_prime = digit
    else:
        non_prime_count += 1

print(f"Prime digits count: {prime_count}")
print(f"Non-prime digits count: {non_prime_count}")

if largest_prime != -1:
    print(f"Largest prime digit: {largest_prime}")
    print(f"Smallest prime digit: {smallest_prime}")
else:
    print("No prime digits found")
