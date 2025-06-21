num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))

print("Before swapping values are num1:",num1," and num2:",num2)
#Swapping of two number by using temp variable
temp = num1
num1 = num2
num2 = temp
print("After swapping values are num1:",num1," and num2:",num2)

#Swapping of two number without using temp variable
num1, num2 = num2, num1
print("Again swapping of values without temp are num1:",num1," and num2:",num2)

#Comparision operations
#Comparing the numbers are +ve or -ve
if (num1 > 0 and num2 > 0):
    print("Both numbers are Positive")
elif (num1 > 0):
    print("Only First is positive")
elif (num2 > 0):
    print("Only Second is positive")
else:
    print("Both numbers are Negative")

#checking the given numbers are Even or Odd
if (num1 % 2 != 0 and num2 % 2 !=  0):
    print("Both numbers are Odd numbers")
elif (num1 % 2 != 0):
    print("First is Odd")
elif (num2 % 2 != 0):
    print("Second is Odd")
else:
    print("Both numbers are Even numbers")

#Finding largets of 3 numbers using if-else condition
if (num1 == num2):
    if (num2 == num3):
        print("All three values are same")
    elif(num2 < num3):
        print(num3, "is the Largest of three")
    else:
        print(num2, "is the Largest of three")
else:
    if(num1 < num2):
        if(num2 < num3):
            print(num3, "is the Largest of three")
        else:
            print(num2, "is the Largest of three")
    else:
        if(num1 < num3):
            print(num3, "is the Largest of three")
        else:
            print(num1, "is the Largest of three")

#Finding largets of 3 numbers using max() function
largest = max(num1, num2, num3)
print(largest, "is the Largest of three values")




