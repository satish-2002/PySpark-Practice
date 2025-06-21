### Python program to add two matrices
mat1 = [[1,2,3],
        [4,5,6],
        [7,8,9]]

mat2 = [[9,8,7],
        [6,5,4],
        [3,2,1]]

if (len(mat1) != len(mat2)) or (len(mat1[0]) != len(mat2[0])):
    print("Matrix addition is not possible for different length matrices")
else:
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j]+mat2[i][j])
        result.append(row)
    print("MATRIX ADDITION RESULT")
    for row in result:
        print(row)