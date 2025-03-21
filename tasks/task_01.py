def pyramid(n):
    for i in range(1, n + 1):
        row = " " * (n - i) + "*" * (2 * i - 1)
        print(row)


# Call the pyramid function with the number of rows
pyramid(5)

# 4 1
# 3 3
# 2 5
# 1 7
# 0 9