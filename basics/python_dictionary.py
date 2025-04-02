# creating a dictionary
sample_dict = {'name': 'John', 'lastname': 'Dutton', 'age': 65, 'city': 'Bozeman', 'state': 'Montana'}

# access the value of the key 'name'
print(sample_dict['name'])  # result is 'John'

# access the value of the key 'lastname'
print(sample_dict['lastname'])  # result is 'Dutton'

# access the value of the key 'age' using get method
print(sample_dict.get('age'))  # result is 65

# get all keys in the dictionary
print(sample_dict.keys())  # result is dict_keys(['name', 'lastname', 'age', 'city', 'state'])

# get all values in the dictionary
print(sample_dict.values())  # result is dict_values(['John', 'Dutton', 65, 'Bozeman', 'Montana'])

# get all items in the dictionary
print(sample_dict.items())  # result is dict_items([('name', 'John'), ('lastname', 'Dutton'), ('age', 65), ('city', 'Bozeman'), ('state', 'Montana')])

# update the value of the key 'city'
sample_dict['city'] = 'Yellowstone'  # result is {'name': 'John', 'lastname': 'Dutton', 'age': 65, 'city': 'Yellowstone', 'state': 'Montana'}

# add a new key 'country' with value 'USA'
sample_dict['country'] = 'USA'  # result is {'name': 'John', 'lastname': 'Dutton', 'age': 65, 'city': 'Yellowstone', 'state': 'Montana', 'country': 'USA'}

# remove the key 'state' from the dictionary
sample_dict.pop('state')  # result is {'name': 'John', 'lastname': 'Dutton', 'age': 65, 'city': 'Yellowstone', 'country': 'USA'}

# remove the last item from the dictionary
sample_dict.popitem()  # result is {'name': 'John', 'lastname': 'Dutton', 'age': 65, 'city': 'Yellowstone'}

# remove all items from the dictionary
sample_dict.clear() # result is {}

# delete the dictionary
del sample_dict  # result is NameError: name 'sample_dict' is not defined

# check if the key 'name' exists in the dictionary
print('name' in sample_dict)  # result is False

# check if the key 'name' does not exist in the dictionary
print('name' not in sample_dict)  # result is True


### METHODS ###

sample_dict = {'name': 'John', 'lastname': 'Dutton', 'age': 65, 'city': 'Bozeman', 'state': 'Montana', 'property': 'Yellowstone Ranch', 'foreman': 'Rip Wheeler', 'ranch_hand': 'Jimmy Hurdstrom', 'daughter': 'Beth Dutton', 'adopted-son': 'Jamie Dutton', 'son': 'Kayce Dutton', 'grandson': 'Tate Dutton', 'friend': 'Thomas Rainwater', 'enemy': 'Dan Jenkins'}

# get the value of the key 'name' using get method
print(sample_dict.get('name'))  # result is None

# get the value of the key 'name' using get method and return 'Not Found' if the key does not exist
print(sample_dict.get('name', 'Not Found'))  # result is 'Not Found'

# remove the last item from the dictionary using popitem method
sample_dict.popitem()  # result is ('enemy', 'Dan Jenkins')

# remove the key 'friend' from the dictionary using pop method
sample_dict.pop('friend')  # result is 'Thomas Rainwater'

# remove the key 'adopted-son' from the dictionary using del method
del sample_dict['adopted-son']  # result is {'name': 'John', 'lastname': 'Dutton', 'age': 65, 'city': 'Bozeman', 'state': 'Montana', 'property': 'Yellowstone Ranch', 'foreman': 'Rip Wheeler', 'ranch_hand': 'Jimmy Hurdstrom', 'daughter': 'Beth Dutton', 'son': 'Kayce Dutton', 'grandson': 'Tate Dutton'}

# remove all items from the dictionary using clear method
sample_dict.clear()  # result is {}

# output the value of the key 'daughter' using get method
print(sample_dict.get('daughter'))  # result is 'Beth Dutton'

# get the keys in the dictionary using keys method
print(sample_dict.keys())  # result is dict_keys(['name', 'lastname', 'age', 'city', 'state', 'property', 'foreman', 'ranch_hand', 'daughter', 'son', 'grandson'])

# get the values in the dictionary using values method
print(sample_dict.values())  # result is dict_values(['John', 'Dutton', 65, 'Bozeman', 'Montana', 'Yellowstone Ranch', 'Rip Wheeler', 'Jimmy Hurdstrom', 'Beth Dutton', 'Kayce Dutton', 'Tate Dutton'])

# get the items in the dictionary using items method
print(sample_dict.items())  # result is dict_items([('name', 'John'), ('lastname', 'Dutton'), ('age', 65), ('city', 'Bozeman'), ('state', 'Montana'), ('property', 'Yellowstone Ranch'), ('foreman', 'Rip Wheeler'), ('ranch_hand', 'Jimmy Hurdstrom'), ('daughter', 'Beth Dutton'), ('son', 'Kayce Dutton'), ('grandson', 'Tate Dutton')])

# retrieve the value of the key 'name' using __getitem__ method
sample_dict.__getitem__('state')  # result is 'Montana'

# return a key iterator using __iter__ method
sample_dict.__iter__()  # result is <dict_keyiterator at 0x7f9f0b9d9b30> Note: can be used in a for loop to iterate over the keys

# return a key iterator using in reversed order using __reversed__ method
sample_dict.__reversed__()  # result is <dict_keyiterator at 0x7f9f0b9d9b30> Note: can be used in a for loop to iterate over the keys in reversed order




