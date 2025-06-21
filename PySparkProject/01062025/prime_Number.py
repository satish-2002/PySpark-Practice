### Prime or not
num = 139

# To check given list of number prime or not
lst = [157,139,237,149,72]

# To check given explicit(Run-time) list of number prime or not
'''lst =[]
count = int(input("Enter number of digits to check prime or not:"))
for x in range(count):
    dig = int(input("Enter list of number:"))
    lst.append(dig)'''
prime_list = []

# To print the prime number within given range
lower = int(input("Enter lower bound value:"))
upper = int(input("Enter lower bound value:"))
prime_list_range =[]

#Checking given number is prime or not
flag = True
if num == 0 or num == 1:
    print(num,"is not a prime number")
else:
    if num > 2:
        for i in range(2,int(num/2)):
            if (num % i) == 0:
                flag = False
                break
if flag:
    print(num,"is a prime number")
else:
    print(num, "is not a prime number")

#Checking given list of number are prime or not
print(lst)
for n in lst:
    if (0<=n<=2) :
        continue
    else:
        if n > 2:
            for i in range(2,int(n/2)):
                if n % i == 0:
                    flag = False
                    break
                else:
                    flag = True
        if flag:
            prime_list.append(n)
print("The prime numbers are",prime_list)

# printing prime number within given range
for n in range(lower, upper+1):
    if (0<=n<=2) :
        continue
    else:
        if n > 2:
            for i in range(2,int(n/2)):
                if n % i == 0:
                    flag = False
                    break
                else:
                    flag = True
        if flag:
            prime_list_range.append(n)
print("The prime numbers are",prime_list_range)