lst = list(map(int, input("N : ").split()))
target = int(input("Target : "))

l, h = 0, len(lst) - 1
result = -1

while l <= h:
    mid = (l + h) // 2
    if lst[mid] == target:
        result = mid
        h = mid - 1   # keep searching left for first occurrence
    elif lst[mid] < target:
        l = mid + 1
    else:
        h = mid - 1

if result != -1:
    print("First occurrence at index:", result)
else:
    print("Target not found")
