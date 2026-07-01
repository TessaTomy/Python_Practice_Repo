# QN: #216 Print Pascal's Triangle

rows = int(input("Enter the number of rows: "))

for i in range(rows):
    print(" " * (rows - i - 1), end="")
    
    val = 1
    for j in range(i + 1):
        print(val, end=" ")
        val = val * (i - j) // (j + 1)
        
    print()
