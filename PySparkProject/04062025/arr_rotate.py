### Python program to rotate the list elements by number of positions
def rotate_array(arr, pos):
    n = len(arr)
    if pos < 0 or pos >= n:
        return "Invalid rotation value"
    # Create an empty array of size n
    rotated_arr = [0] * n
    for i in range(n):
        rotated_arr[i] = arr[(i + pos) % n]
    return rotated_arr

def split_and_add(arr, pos):
    n = len(arr)
    if pos <= 0 or pos >= n:
        return arr
    first_part = arr[:pos]
    second_part = arr[pos:]
    result_s = second_part+first_part
    return result_s

arr = list(map(int, input("Enter array elements separated by space: ").split()))
pos = int(input("Enter number of positions that array should rotate:"))

result = rotate_array(arr, pos)
res = split_and_add(arr, pos)
print("Before Rotation Array:", arr)
print("After Rotation Array:", result)
print("After Split and Add:", res)