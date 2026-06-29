#144 Find the largest power of 3 less than N

import math

def largest_power_of_three(n):
    if n <= 1:
        return "No power of 3 is less than this number."
        
    if n == int(n):
        n -= 0.00001
        
    exponent = math.floor(math.log(n, 3))
    return 3 ** exponent

number = float(input("Enter a number: "))
print(f"Result: {largest_power_of_three(number)}")
