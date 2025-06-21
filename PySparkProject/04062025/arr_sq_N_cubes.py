###Python program to print array squares of N natural numbers.

arr = list(map(int,input("Enter array elements:").split(",")))
squares = []
cubes = []

for i in arr:
    squares.append(i**2)
    cubes.append(i**3)

print("Squares of array is:", squares)
print("Cubes of array is:", cubes)