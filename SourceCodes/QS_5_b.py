def pascal_triangle_pattern(n):
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(row[j - 1] * (i - j + 1) // j)
        print(" "*(n-i-1), row)

if __name__ == '__main__':
    while True:
        n = int(input("Enter the number of rows: "))
        pascal_triangle_pattern(n)
        ch = int(input("Do you want to insert again?[1-yes/0-no]: "))
        if ch == 0:
            break
