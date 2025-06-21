###Python program to print even, odd, prime numbers in the array list
arr = list(map(int, input("Enter array elements separated by space: ").split()))

even = []
odd = []
non_prime = []
prime = []
for i in arr:
    if i <= 0:
        print("Enter positive numbers")
    else:
        for j in range(2, i):
            if (i % j) == 0:
                print(i)
                non_prime.append(i)
                break
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

prime = [n for n in arr if n not in non_prime]
print("Even numbers in the array are:", even)
print("Odd numbers in the array are:", odd)
print("Non-prime numbers in the array are:", non_prime)
print("Prime numbers in the array are:", prime)