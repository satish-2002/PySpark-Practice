###Python program to find Simple and Compound interest

#Simple interest SI = (P * T * R)/100
#Compound interest CI = P(1 + R/n)^n*t

P = float(input("Enter principal amount(investment amount):"))
R = float(input("Enter rate of interest:"))
T = float(input("Enter number of years:"))
n = float(input("Enter number of time compounded:"))

SI = (P*T*R)/100
CI = P*((1+(R/100)/n)**(n*T))

print(f"Simple interest for the {P} in {T} years with {R} interest is :{SI}")
print(f"Compound interest for the {P} in {T} years with {R} interest is :{CI}")