Details ={ 'Siva':{'Gender':'Male','Age':27,'Address':'Pithapuram','Mobile':'8965432147'},
           'Satish':{'Gender':'Male','Age':24,'Address':'Kakinada','Mobile':'8919903684'},
           'Surya':{'Gender':'Male','Age':23,'Address':'Kakinada','Mobile':'9391231991'},
           'Satya':{'Gender':'Female','Age':23,'Address':'Rajamundry','Mobile':'9567890432'},
           'Supriya':{'Gender':'Female','Age':22,'Address':'Rajamundry','Mobile':'8978685848'},
           'Chaitanya':{'Gender':'Female','Age':15,'Address':'Turangi','Mobile':'7879767574'},
           'Anjali':{'Gender':'Female','Age':14,'Address':'Turangi','Mobile':'9292929292'}}

Districts = {'Kakinada':'533001','Pithapuram':'533102','Rajamundry':'522002','Turangi':'533014'}
Males = []
Females = []

for i,j in Details.items():
    if j['Address'] in Districts:
        j['Pincode'] = Districts[j['Address']]
    if j['Gender'] == 'Male':
        Males.append(i)
    else:
        Females.append(i)
print("Males:", Males)
print("Females:", Females)
for member, details in Details.items():
    print(member,":",details)
