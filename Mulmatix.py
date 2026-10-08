rows1 = int(input("Enter number of rows for first matrix: "))
cols1 = int(input("Enter number of columns for first matrix: "))
rows2 = int(input("Enter number of rows for second matrix: "))
cols2 = int(input("Enter number of columns for second matrix: "))

if cols1 != rows2:
    print("Matrix multiplication not possible")
    exit()

print("Enter elements of first matrix:")
matrix1 = [[int(input()) for _ in range(cols1)] for _ in range(rows1)]

print("Enter elements of second matrix:")
matrix2 = [[int(input()) for _ in range(cols2)] for _ in range(rows2)]

result = [[0 for _ in range(cols2)] for _ in range(rows1)]

for i in range(rows1):
    for j in range(cols2):
        for k in range(cols1):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

print("Product of the two matrices is:")
for row in result:
    print(row)
