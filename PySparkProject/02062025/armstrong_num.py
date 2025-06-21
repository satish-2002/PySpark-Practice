### Python program to check armstrong number or not
num = number = int(input("Enter a number:"))
power = len(str(num))
sum_of_digits = 0

#To check weather given number is armstrong or not
if num < 0:
    print("Can't find armstrong number for negative numbers")
else:
    while num > 0:
        digit = num % 10
        sum_of_digits = sum_of_digits + int(digit)**power
        num = num // 10
if number == sum_of_digits:
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")

#Printing armstrong numbers between range
lower = int(input("Enter lower bound number:"))
upper = int(input("Enter upper bound number:"))

for i in range(lower, upper+1):
    num = number = i
    power = len(str(num))
    sum_of_digits = 0
    if number < 0:
        print("Can't find armstrong number for negative numbers")
    else:
        while num > 0:
            digit = num % 10
            sum_of_digits = sum_of_digits + int(digit) ** power
            num = num // 10
    if number == sum_of_digits:
        print(number)