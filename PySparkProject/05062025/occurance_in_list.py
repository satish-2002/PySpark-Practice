###Python program to print the element and count of occurrence in the list
arr = list(map(int, input("Enter array elements separated by comma: ").split(",")))
#alpha_arr = input("Enter single characters separated by comma:").split(",")           # INPUT : A, P, P, L, E, I, S, A, F, R, U, I, T
alpha_arr = ['A', 'P', 'P', 'L', 'E', 'I', 'S', 'A', 'F', 'R', 'U', 'I', 'T']
#arr = [4, 8, 8, 99, 100, 37, 98, 37, 2, 7, 5, 7]
string = input("Enter words separated by space:").split()
sort_arr = sorted(arr)
print(sort_arr)
num_dict_array = {}
for i in sort_arr:
    if i in num_dict_array:
        num_dict_array[i] = num_dict_array[i] + 1
    else:
        num_dict_array[i] = 1

alpha_dict_array = {}
for i in alpha_arr:
    if i in alpha_dict_array:
        alpha_dict_array[i] = alpha_dict_array[i] + 1
    else:
        alpha_dict_array[i] = 1

word_dict_array = {}
for i in string:
    if i in word_dict_array:
        word_dict_array[i] = word_dict_array[i] + 1
    else:
        word_dict_array[i] = 1

print(num_dict_array)
print(alpha_dict_array)
print(word_dict_array)