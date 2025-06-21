### To print factorial of a given number

num = int(input("Enter a value:"))
factorial = 1
# using normal method
if num < 0:
    print("No factorial for Negative numbers")
elif num == 0:
    print("Factorial of Zero is 1")
else:
    for i in range(2,num+1):
        factorial = factorial*i
    print(f"Factorial of {num} is {factorial}")

# using recursive method
def recur_fact(n):
    if n == 1:
        return 1
    else:
        return n*recur_fact(n-1)
print(f"Factorial of {num} using recursion is :", recur_fact(num))