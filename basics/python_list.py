sample_list = ['d', 'i', 's', 'c', 'o', 'g', 'o', 'o', 'd']

# print the length of the list using len function
print(len(sample_list)) # result is 9

# print the length of the list using __len__ method
print(sample_list.__len__())

# print all values in the list
print(sample_list)  # result is ['d', 'i', 's', 'c', 'o', 'g', 'o', 'o', 'd']

# print all values in the list using slicing
print(sample_list[:])  # result is ['d', 'i', 's', 'c', 'o', 'g', 'o', 'o', 'd']

# print all values in the list using slicing
print(sample_list[0:9])  # result is ['d', 'i', 's', 'c', 'o', 'g', 'o', 'o', 'd'] (note: 9 is the length of the list)

# print the first item in the list using indexing
print(sample_list[0])  # result is d

# print the last item in the list using indexing
print(sample_list[-1])  # result is d
print(sample_list[8])  # result is d (note: 8 is the index of the last item in the list based on 0-8 index)

# print the last item of the list using slicing
print(sample_list[-1:])  # result is ['d']

# print the first 3 items in the list using slicing
print(sample_list[:3])  # result is ['d', 'i', 's']

# compare the list with another list
compare_list = ['d', 'i', 's', 'c', 'o', 'g', 'o', 'o', 'd']
print(sample_list == compare_list)  # result is True
print(sample_list.__eq__(compare_list))  # result is True
print(sample_list.__ne__(compare_list))  # result is False
print(sample_list.__le__(compare_list))  # result is True
print(sample_list.__ge__(compare_list))  # result is True
print(sample_list.__gt__(compare_list))  # result is False
print(sample_list.__lt__(compare_list))  # result is False

# extend list with another list
sample_list.extend(['g', 'o', 'o', 'd'])
print(sample_list)  # result is ['d', 'i', 's', 'c', 'o', 'g', 'o', 'o', 'd', 'g', 'o', 'o', 'd']

# add an item to the list using append method
sample_list.append('s')

# add an item to the list using insert method
sample_list.insert(0, 'a')  # insert 'a' at the beginning of the list
print(sample_list)  # result is ['a', 'd', 'i', 's', 'c', 'o', 'g', 'o', 'o', 'd', 'g', 'o', 'o', 'd', 's']

# remove an item from the list
sample_list.remove('a')  # removes the first instance of 'a' from the list using remove method
del sample_list[0]  # remove 'a' from the list using del function
sample_list.__delitem__(0)  # removes the first item from the list using __delitem__ method
sample_list.pop(0)  # remove 'a' from the list using pop method. if no index is provided, it removes the last item in the list
print(sample_list)  # result is ['d', 'i', 's', 'c', 'o', 'g', 'o', 'o', 'd', 'g', 'o', 'o', 'd', 's']

# remove all instance of element 'o' from the list
while 'o' in sample_list:
    sample_list.remove('o')  # using while loop

sample_list = [letter for letter in sample_list if letter != 'o']  # using list comprehension

sample_list = list(filter(lambda letter: letter != 'o', sample_list))  # using filter function

# re-arrange list in reverse order
sample_list.reverse()  # result is ['d', 'o', 'o', 'g', 'o', 'c', 's', 'i', 'd'] using reverse method - note: this changes the original list
sample_list = sample_list[::-1]  # result is ['d', 'i', 's', 'c', 'o', 'g', 'o', 'o', 'd'] using slicing
sample_list = sorted(sample_list, reverse=True)  # result is reversed alphabetical ['s', 'o', 'o', 'o', 'i', 'g', 'd', 'd', 'c'] using sorted function
sample_list.sort(reverse=True)  # result is result is reversed alphabetical ['d', 'o', 'o', 'g', 'o', 'c', 's', 'i', 'd'] using sort method

# move the last item to the beginning of the list
sample_list.insert(0, sample_list.pop())  # result is ['d', 'd', 'i', 's', 'c', 'o', 'g', 'o', 'o']

# move the first item to the end of the list
sample_list.append(sample_list.pop(0)) # result is ['i', 's', 'c', 'o', 'g', 'o', 'o', 'd', 'd']

# count the number of times 'o' appears in the list
print(sample_list.count('o'))  # result is 3

# find the index of 'o' in the list
print(sample_list.index('o'))  # result is 4

# find the index of 'o' in the list starting from index 5
print(sample_list.index('o', 5))  # result is 6

# find the index of 'o' in the list starting from index 7 to 8
print(sample_list.index('o', 7, 8))  # result is 7

# clear the list
sample_list.clear()  # result is []

# rest the list to the original list
sample_list = ['d', 'i', 's', 'c', 'o', 'g', 'o', 'o', 'd']

# MODIFICATION: add a new item to the list
sample_list.append('s')

# MODIFICATION: remove the first item from the list
sample_list.pop(0)

# MODIFICATION: remove the last item from the list
sample_list.pop()

# MODIFICATION: remove the first instance of 'o' from the list
sample_list.remove('o')

# MODIFICATION: change the first item in the list to 'a'
sample_list[0] = 'a'

# MODIFICATION: insert multiple items at the beginning of the list using slicing
sample_list[0:2] = ['b', 'c']  # result is ['b', 'c', 's', 'c', 'o', 'g', 'o', 'o', 'd']
sample_list[0:2] = ['d', 'i']  # result is ['d', 'i', 's', 'c', 'o', 'g', 'o', 'o', 'd']

# MODIFICATION: remove multiple items from the list using slicing
sample_list[0:2] = []  # result is ['s', 'c', 'o', 'g', 'o', 'o', 'd']






