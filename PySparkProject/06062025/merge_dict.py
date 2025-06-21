### Python program to merge dictionaries
class1 = {'CM-239':'siva','CM-227':'satish','CM-235':'surya','CM-214':'satya'}
class2 = {'CM-231':'supriya','CM-257':'chaitanya','CM-221':'anjali'}

key_values = [(key, value) for key, value in class1.items()]            #Converted dictionary into list of tuples
print("key_values(tuples):",key_values)

class1.update(class2)                                                   #Merge dictionaries
print("Students Data:",class1)

sorted_dict = dict(sorted(class1.items(), key=lambda item: item[1]))    #Sort dictionaries
inverted_dict = {v: k for k, v in sorted_dict.items()}                  #invert dictionary
print("Sorted order(names):",inverted_dict)

Annual = { 'siva':{'Telugu':83,'Hindi':87,'English':82,'Maths':75,'EVS':78},
           'satish':{'Telugu':89,'Hindi':82,'English':78,'Maths':92,'EVS':97},
           'surya':{'Telugu':73,'Hindi':72,'English':82,'Maths':89,'EVS':87},
           'satya':{'Telugu':92,'Hindi':85,'English':96,'Maths':99,'EVS':89},
           'supriya':{'Telugu':94,'Hindi':80,'English':88,'Maths':82,'EVS':87},
           'chaitanya':{'Telugu':90,'Hindi':82,'English':88,'Maths':92,'EVS':77},
           'anjali':{'Telugu':81,'Hindi':80,'English':85,'Maths':62,'EVS':97}}

'''results0 = {}
for name,marks in Annual.items():
    results01 = {name: sum(marks.values())}
    results0.update(results01)
print(results0)'''

results = {name: sum(marks.values()) for name, marks in Annual.items()}
print("Results:",results)

Ranks = dict(sorted(results.items(), key=lambda item: item[1],reverse = True))
print("Ranks:",Ranks)



for (i, j),(x,y),(a,b) in zip(class1.items(),results.items(),Ranks.items()):
    rank = {j, next((i for i, (k, v) in enumerate(Ranks.items()) if v == Ranks[j]), None) + 1}
    details = {"id": i, "Total": Ranks[j], "Rank": next((i for i, (k, v) in enumerate(Ranks.items()) if v == Ranks[j]), None) + 1}
    progress = {x:details}
    print(progress)