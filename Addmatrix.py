rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements of first matrix:")
matrix1 = [[int(input()) for _ in range(cols)] for _ in range(rows)]

print("Enter elements of second matrix:")
matrix2 = [[int(input()) for _ in range(cols)] for _ in range(rows)]

result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]

print("Sum of the two matrices is:")
for row in result:
    print(row)
