### Python program to print multiplication table

number = int(input("Enter number of which table:"))
nterms = int(input("Enter nth term of the table:"))

for i in range(1, nterms+1):
    print(f"{number} * {i} =", number*i)

#To print the multiplication with lower and upper bounds
lower = int(input("Enter lower bound of the table:"))
upper = int(input("Enter upper bound of the table:"))

for i in range(lower, upper+1):
    print(f"{number} * {i} =", number*i)