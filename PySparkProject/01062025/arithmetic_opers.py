# Python program on Arithmetic Operators

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

#Addition
print("Addition of ",num1," and ",num2,":",num1+num2)

#Subtraction
print("Subtraction of ",num1," and ",num2,":",num1-num2)

#Multiplication
print("Multiplication of ",num1," and ",num2,":",num1*num2)

#Division
if(num2 == 0):
    print("Zero Division error")
else:
    print("Division of ",num1," and ",num2,":",num1/num2)

#Remainder division / modulo division
if(num2 == 0):
    print("Zero Division error")
else:
    print("Modulo Division of ",num1," and ",num2,":",num1%num2)

#Floor division
if(num2 == 0):
    print("Zero Division error")
else:
    print("Floor Division of ",num1," and ",num2,":",num1//num2)

#Power of
print("Power of ",num1," and ",num2,":",num1**num2)