### Python Program to print squares and cubes within given range
num = int(input("Enter number of elements:"))
squares = []
cubes = []

#To print squares and cubes within bound range
start = int(input("Enter start range:"))
end = int(input("Enter end range:"))

#To print squares and cubes within given range
for i in range(1, num+1):
#To print squares and cubes within bound range
#for i in range(start, end+1):
    squares.append(i**2)
    cubes.append(i**3)

print("Squares with in given range:",squares)
print("Cubes with in given range:",cubes)

