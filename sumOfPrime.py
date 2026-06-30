#149 Find the sum of prime digits in a number

def all_digits_prime(n: int) -> bool:
    prime_digits = {'2', '3', '5', '7'}
    return sum(int(digit) for digit in str(n) if digit in prime_digits)

all_digits_prime(int(input("Enter a number: ")))
