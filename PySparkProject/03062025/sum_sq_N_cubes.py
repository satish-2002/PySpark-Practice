###Python program to print squares and cubes of an array elements

n = int(input("Enter N value:"))

if n <= 0:
    print("Enter positive number")
else:
    print(f"Sum of squares of {n} is : ", sum(i**2 for i in range(n+1)))
    print(f"Sum of cubes of {n} is : ", sum(i**3 for i in range(n+1)))