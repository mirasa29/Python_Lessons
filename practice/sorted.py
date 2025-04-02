# sample list dictionary
people = [
    {"name": "Kevin Bacon", "age": 61},
    {"name": "Fred Ward", "age": 77},
    {"name": "finn Carter", "age": 59},
    {"name": "Ariana Richards", "age": 40},
    {"name": "Victor Wong", "age": 74},
    {"age": 74},
]

# sort the list of dictionary by name key
sort_people = sorted(people, key=lambda p: p['name'].lower())
# print(sort_people) # [{'name': 'Ariana Richards', 'age': 40}, {'name': 'Fred Ward', 'age': 77}, {'name': 'Kevin Bacon', 'age': 61}, {'name': 'Victor Wong', 'age': 74}, {'name': 'finn Carter', 'age': 59}]

# sort the list of dictionary by name key and standardize the case of the name
sort_pip = sorted(people, key=lambda p: p['name'].upper())
up_sort_pip = [{'name': p['name'].upper(), 'age': p['age']} for p in sort_pip]
# print(up_sort_pip) # [{'name': 'ARIANA RICHARDS', 'age': 40}, {'name': 'FINN CARTER', 'age': 59}, {'name': 'FRED WARD', 'age': 77}, {'name': 'KEVIN BACON', 'age': 61}, {'name': 'VICTOR WONG', 'age': 74}]

# return the list of dictionary where name key exists and standardize the case of the name to upper
up_sort_pip = [{'name': p['name'].upper(), 'age': p['age']} for p in sort_pip if 'name' in p]


# map the list of dictionary and return in format "name is age years old"
name_declarations = list(map(lambda p: f"{p['name']} is {p['age']} years old", sort_people))
print(name_declarations)

# filter list of dictionary where age is less than 70 and return in ascending order based on age
under_seventy = sorted(list(filter(lambda p: p['age'] < 70, sort_people)), key=lambda p: p['age'])
print(under_seventy)
