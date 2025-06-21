###Python Program to find sum of array elements

arr1 = [5,10,20,40,80]
#To pass array elements at run time
arr2 = list(map(int,input("Enter array elements:").split(",")))

#Sum of fixed array elements
sum_arr = sum(arr1)
print("Sum of fixed array elements is:", sum_arr)

#Sum of variable array(Explicit) elements
sum_array = 0
for i in arr2:
    sum_array = sum_array+i
print("Sum of array elements is:", sum_array)

#Sum of fixed nested array elements
nest_arr = [[30,23,12,13,22],[23,27]]
flat_list = [num for subarr in nest_arr for num in subarr]
final_sum = sum(flat_list)
print("Sum of nested array elements is:", final_sum)

#Sum of partially nested array elements
flat_list = []
for item in nest_arr:
    if isinstance(item, list):
        flat_list.extend(item)  # unpack nested list
    else:
        flat_list.append(item)
total_sum = sum(flat_list)
print("Sum of partially nested array elements:", total_sum)