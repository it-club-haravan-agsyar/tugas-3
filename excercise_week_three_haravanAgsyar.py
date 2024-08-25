groupName = [
    {'name': 'Haravan Agsyar', 'age': 15, 'grade':10},
    {'name': 'Fakhri', 'age': 17, 'grade':11},
    {'name': 'Asep', 'age': 17, 'grade':11}
]
for index, obj in enumerate(groupName):
    print(f"{index + 1}. {obj['name']} is {obj['age']} years old and currently in grade {obj['grade']}")