mydic = {1: 'Anu'}
print('Dictionary is: ', mydic)

mydic1 = {'Address': [1, 2, 3, 4, 5]}
print(mydic1)
print(mydic1['Address'])

a = {"Name": "Abhijith", "Age": 25}
print(a)
print(a["Name"])
print(a["Age"])
print()

a["Course"] = "Python"      # ADDING ELEMENTS
print(a)

a["Name"] = "Athira"        # UPDATING
print("After updation:", a)
print()

a.update({'Age': 30})       # update() METHOD
print(a)

# DELETE ELEMENTS
b = {'Name': 'Athira', 'Age': 25, 'Course': 'Python'}
del b["Age"]        # del KEYWORD
print(b)

b.pop("Name")       # pop() METHOD
print(b)
print()

DIC = {1: 'Anu', 2: 'Athira', 3: 'Renya', 4: 'Bibin', 5: 'Shone'}
print(DIC)

for i in DIC:
    print(i)
print()
for i in DIC.items():
    print(i)
    print()
print()
for i in DIC.values():
    print(i)
print()
for i in DIC.keys():
    print(i)
print()
for i in DIC:
    print(DIC[i])
