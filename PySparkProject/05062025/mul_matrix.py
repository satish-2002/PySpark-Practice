### Python program to multiply two matrices
mat1 = [[1,2,3],
        [4,5,6]]

mat2 = [[6,5],
        [4,3],
        [2,1]]

rowm1 = len(mat1)
colm1 = len(mat1[0])
rowm2 = len(mat2)
colm2 = len(mat2[0])

if (colm1 != rowm2):
    print("Matrix addition is not possible for different length matrices")
else:
    result = [[0 for _ in range(colm2)]for _ in range(rowm1)]
    for i in range(rowm1):
        for j in range(colm2):
            for k in range(colm1):
                result[i][j] = result[i][j] + mat1[i][k] * mat2[k][j]
    print("MATRIX MULTIPLICATION RESULT")
    for row in result:
        print(row)

