# Question: Find the largest power of 2 less than n using the shortest bitwise method.

def largest_power(n):
    n = int(n) - 1 if n == int(n) else int(n)
    return 1 << (n.bit_length() - 1)

number = float(input("Enter a number: "))
print(f"Result: {largest_power(number)}")
