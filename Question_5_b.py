row = int(input("Enter the Number of rows: "))

for i in range(row + 1):
    p = 1
    for j in range(row):
        print(end = " ")
    for k in range(i + 1):
        print(p, end = " ")
        p = (p * (i - k) // (k + 1))
    row -= 1
    print()