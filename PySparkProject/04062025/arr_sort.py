###Python program to sort the array in ascending and descending order
# Take input from user
arr = list(map(int, input("Enter array elements separated by space: ").split()))
n = len(arr)
order = input("Enter sorting order (asec or desc):")
for i in range(n):
    for j in range(0, n-i-1):
        if order == 'asec':
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        elif order == 'desc':
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        else:
            print("Enter correct order method")

print("Sorted array is order:", arr)

#simple way
asec_arr = sorted(arr)
print(asec_arr)
desc_arr = sorted(arr, reverse=True)
print(desc_arr)