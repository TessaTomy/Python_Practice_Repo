n = int(input("Enter a number: "))

num_str = str(abs(n))
is_alternating = True

for i in range(len(num_str) - 1):
    current_digit = int(num_str[i])
    next_digit = int(num_str[i + 1])
    
    # If both are even or both are odd, their sum is always even
    if (current_digit + next_digit) % 2 == 0:
        is_alternating = False
        break

if is_alternating:
    print("Digits alternate between even and odd")
else:
    print("Digits do not alternate")
