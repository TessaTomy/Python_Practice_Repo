#167 Check if a number can be expressed as the sum of two primes


def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

N = int(input("N: "))

can_be_sum = False

if N > 3:
    for i in range(2, (N // 2) + 1):
        if is_prime(i) and is_prime(N - i):
            can_be_sum = True
            print(f"Yes: {N} = {i} + {N - i}")
            break

if not can_be_sum:
    print("No")
