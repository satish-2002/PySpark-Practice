### Python Program to find the HCF of two and three numbers

#HCF of 2 numbers using UDF
def compute_hcf2(n1, n2):
    smaller = min(n1, n2)
    for i in range(1, smaller+1):
        if((n1 % i == 0) and (n2 % i == 0)):
            hcf = i
    return hcf

num1, num2 = map(int,input("Enter 2 numbers for HCF:").split())
print(f"HCF of {num1} and {num2} is : ", compute_hcf2(num1,num2))

#HCF of 3 numbers using UDF
def compute_hcf3(n1, n2, n3):
    smaller = min(n1, n2, n3)
    for i in range(1, smaller+1):
        if((n1 % i == 0) and (n2 % i == 0) and (n3 % i == 0)):
            hcf = i
    return hcf

num1, num2, num3 = map(int,input("Enter 3 numbers for HCF:").split())
print(f"HCF of {num1}, {num2} and {num3} is : ", compute_hcf3(num1,num2,num3))

def find_gcd(n1, n2):
    while(n2 != 0):
        n1, n2 = n2, n1 % n2
    return n1

def find_gcd_3(n1, n2, n3):
    return find_gcd(find_gcd(n1,n2),n3)

print(f"GCD of {num1}, {num2} and {num3} is : ", find_gcd_3(num1,num2,num3))