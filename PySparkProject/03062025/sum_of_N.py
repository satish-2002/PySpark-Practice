### Python Program to print sum of N natural numbers
#using formula
num = int(input("Enter Nth number:"))
sumN = int(num*(num+1))/2
print(f"Sum of {num} numbers : {sumN}")

#using for loop
sum = 0
for i in range(1, num+1):
    sum = sum+i
print(sum)

