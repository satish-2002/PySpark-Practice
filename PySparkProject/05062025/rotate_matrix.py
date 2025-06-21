### Python program to print transpose of a matrix
import numpy as np

## To create matrix explicitly
rows = int(input("Enter no. of rows:"))
cols = int(input("Enter no. of columns:"))
n = rows * cols
values = list(map(int, input("Enter array elements separated by space: ").split()))
if len(values) == n:
    matrix = np.array(values).reshape(rows, cols)
else:
    print("There is count mismatch between rows and columns with values entered, PLEASE CHECK")
    exit(1)
print("MATRIX CREATED")
print(matrix)

result = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]

matrix1 = [[1,2,3],
           [4,5,6],
           [7,8,9]]
revered_matrix = matrix1[::-1]
result = [list(row) for row in zip(*revered_matrix)]    # when we pass numpy created matrix output returns odd because the input matrix is created by numpy

rotated = np.rot90(matrix, -1)

print("ROTATE 90 MATRIX RESULT")
for row in result:
    print(row)

print("ROTATE 90 WITH NUMPY RESULT")
for row in rotated:
    print(row)

