#################### Tupple ####################

# create a tuple
t = (1, 2, 3, 4, 5)

# access the first item in the tuple
print(t[0])  # result is 1

# access the last item in the tuple
print(t[-1])  # result is 5

# access the first two items in the tuple
print(t[0:2])  # result is (1, 2)

# access the last three items in the tuple
print(t[-3:])  # result is (3, 4, 5)

# add a new item to the tuple
t = t + (6,)  # result is (1, 2, 3, 4, 5, 6)

### METHODS ###

# count the number of times 3 appears in the tuple
print(t.count(3))  # result is 1

# find the index of 3 in the tuple
print(t.index(3))  # result is 2

# find the index of 3 in the tuple starting from index 2
print(t.index(3, 2))  # result is 2



#################### Ranges ####################

# creating a range
r = range(0, 6)  # result is range(0 6)

# access the first item in the range
print(r[0])  # result is 1

# access the last item in the range
print(r[-1])  # result is 5

# make a list from the range
r_list = list(r)  # result is [0. 1, 2, 3, 4, 5]

# extend the range
r = range(0, 10)  # result is range(0, 10)

# create a range with a step of 2
r = range(0, 10, 2)  # result is range(0, 10, 2)
samp_list = list(r)  # result is [0, 2, 4, 6, 8]

# create a reversed range with a step of -1
r1 = range(10, 0, -1)  # result is range(10, 0, -1)
sample_list = list(r1)  # result is [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

### METHODS ###

# find the index of 3 in the range
print(r.index(3))  # result is 3

# count the number of times 3 appears in the range
print(r.count(3))  # result is 1

# find the index of 3 in the range starting from index 2
print(r.index(3, 2))  # result is 3

# find the index of 3 in the range starting from index 2 to 4
print(r.index(3, 2, 4))  # result is 3



