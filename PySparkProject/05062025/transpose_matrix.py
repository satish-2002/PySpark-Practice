### Python program to print transpose of a matrix
import numpy as np

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

result = [[0 for _ in range(len(mat))] for _ in range(len(mat[0]))]

for i in range(len(mat)):
    for j in range(len(mat[0])):
        result[j][i] = mat[i][j]

print("TRANSPOSE MATRIX RESULT")
for row in result:
    print(row)

## To create matrix explicitly
rows = int(input("Enter no. of rows:"))
cols = int(input("Enter no. of columns:"))
n = rows * cols
values = list(map(int, input("Enter array elements separated by space: ").split()))
if len(values) == n:
    print("MATRIX CREATED")
    matrix = np.array(values).reshape(rows, cols)
else:
    print("There is count mismatch between rows and columns with values entered, PLEASE CHECK")
    exit(1)
print(matrix)