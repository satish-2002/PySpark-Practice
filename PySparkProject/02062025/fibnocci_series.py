### Python Program to print fibonacci series

nterm = int(input("Enter number of elements:"))
n1,n2 = 0,1
count = 1
fibonacci_lst=[0,1]

#Fibonacci series using while loop
if nterm < 0:
    print("Fibonacci series is not possible for Negative numbers")
elif nterm == 0 or nterm == 1:
    print(f"Fibonacci for {nterm} is :{nterm}")
else:
    while count<nterm-1:
        nth = n1+n2
        fibonacci_lst.append(nth)
        n1,n2 = n2,nth
        count = count+1
    print(fibonacci_lst)

#Fibonacci series using for loop and UDF
def fibonacci_series(n):
    fib = []
    a, b = 0, 1
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b
        #if len(fib) == n:                                        # To print direct fibonacci value
        #   return fib[-1]
    return fib                                                    # To print fibonacci series of n terms

if nterm < 0:
    print("Fibonacci series is not possible for Negative numbers")
else:
    print(f"Fibonacci series :", fibonacci_series(nterm))         #To print Fibonacci series of N terms
    #print(f"Fibonacci of {nterm} is :",fibonacci_series(nterm))  #To print Fibonacci of nth term directly

# using recursive method
def recur_fib(n):
    if n <= 1:
        return n
    else:
        return (recur_fib(n-1)+recur_fib(n-2))

if nterm < 0:
    print("Please enter positive number")
else:
    for i in range(nterm):
        print(recur_fib(i))
print(f"Fibonacci series of {nterm} using recursion is :", recur_fib(nterm-1))