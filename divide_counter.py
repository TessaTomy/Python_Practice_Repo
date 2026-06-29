#143 Count how many times a number can be divided by 2
def count_divisions(n):
    steps = 0
    while n > 1:
        n = n / 2
        steps += 1
    return steps

number = float(input("Enter a number: "))
print(f"Can be divided: {count_divisions(number)} times")
