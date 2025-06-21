### Python Program to find the LCM of two and three numbers
import math

#LCM of 2 number using UDF
def compute_lcm2(n1, n2):
    if n1 > n2:
        greater = n1
    else:
        greater = n2
    while(True):
        if((greater % n1 == 0) and (greater % n2 == 0)):
            lcm = greater
            break
        greater = greater + 1
    return lcm

num1, num2 = map(int,input("Enter 2 numbers for LCM:").split())
print(f"LCM of {num1} and {num2} is : ", compute_lcm2(num1,num2))

#LCM of 2 number using UDF
def compute_lcm3(n1, n2, n3):
    greater = max(n1, n2, n3)
    while(True):
        if((greater % n1 == 0) and (greater % n2 == 0) and (greater % n3 == 0)):
            lcm = greater
            break
        greater = greater + 1
    return lcm

num1, num2, num3 = map(int,input("Enter 3 numbers for LCM:").split())
print(f"LCM of {num1},{num2} and {num3} is : ", compute_lcm3(num1,num2,num3))


#LCM with math function
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Function to find LCM of 3 numbers
def lcm_of_three(x, y, z):
    return lcm(lcm(x, y), z)

# Calculate LCM
result = lcm_of_three(num1, num2, num3)
print(f"LCM of {num1},{num2} and {num3} is : {result}")

def find_gcd(n1, n2):
    while(n2 != 0):
        n1, n2 = n2, n1 % n2
    return n1

def find_gcd_3(n1, n2, n3):
    return find_gcd(find_gcd(n1,n2),n3)

