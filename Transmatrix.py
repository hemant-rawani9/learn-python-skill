rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements of the matrix:")
matrix = [[int(input()) for _ in range(cols)] for _ in range(rows)]

transpose = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

print("Transpose of the matrix is:")
for row in transpose:
    print(row)
