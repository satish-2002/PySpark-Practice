# program to create nested dictionary explicitly taken inputs from user
size = int(input("Enter the size:"))
id = []
for i in range(size):
    a = int(input("Enter id :"))
    id.append(a)
l = ['Name', 'Father_name', 'Address']
dicts = [{} for _ in range(size)]
for a,i in zip(dicts,id):
    for b in l:
        k = input(f"Enter {b} for {i} :")
        a[b] = k

data = dict(zip(id, dicts))
print(data)