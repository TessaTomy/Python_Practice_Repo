num = int(input("Enter a number: "))

if num < 1:
    is_abundant = False
else:
    divisor_sum = 0
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            divisor_sum += i

    is_abundant = divisor_sum > num

if is_abundant:
    print(f"{num} is an Abundant Number!")
else:
    print(f"{num} is NOT an Abundant Number.")
