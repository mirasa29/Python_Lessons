########## simple function and lambda ##########

# sample function
def square(num):
    return num * num

# calling
samp1 = square(2)

# equivalent in lambda
t = lambda x: x * x

# calling
samp2 = t(2)

# test
assert samp1 == samp2


########## High order functions ##########

from functools import reduce # as the reduce function no longer built-in function in python 3

# high order functions (map, filter, reduce)

samp_list = [1, 2, 3, 4, 5] # sample list

# MAP: mapping values to an action and returning the same number of items
let_square = map(lambda num: num * num, samp_list)
# print(list(let_square)) <-- This prints the result as a list once but will not be able to print again as the map object is exhausted
# print(list(map(lambda num: num * num, samp_list))) <-- This prints results every time it is called WITHOUT exhausting the map object

# long version using named function:
def square_list(list):
    ctr = 0
    for i in samp_list:
        samp_list[ctr] = i * i
        ctr += 1
        if ctr == len(samp_list):
            break

# square_list(samp_list) <-- This will change the original list based on the function
# print(samp_list) <-- This will print the modified list


# FILTER: iterate through vals and getting outcome based on a condition
filter_me = filter(lambda num: num % 2 == 0, samp_list)
# print(list(filter_me)) <-- This prints the result as a list once but will not be able to print again as the filter object is exhausted
# print(list(filter(lambda num: num % 2 == 0, samp_list))) <-- This prints results every time it is called WITHOUT exhausting the filter object

# long version using named function:
def filter_list(list):
    n_list = []
    for i in list:
        if i % 2 == 0:
            n_list.append(i)
    return n_list

# filter_list(samp_list)) <-- This returns the new list based on the function


# reduce iterate through vals and aggregate/accumulate to a final single result
reduce_me = reduce(lambda acc, num: acc + num, samp_list, 0)
# print(reduce_me)

# long version using named function:
def reduce_list(list):
    acc = 0
    for i in list:
        acc = acc + i
    return acc

# reduce_list(samp_list)


########## container methods and function ##########

samp_words = ['dust', 'Jagger', 'arrow', 'BAss', 'feet', 'CACTUS', 'Abbey', 'BROWN', 'DesTiny', 'element', 'Gag', 'East', 'Host', 'Crystal', 'INVOKE', 'JUMPER']

# sorted: accepts a list and returns it sorted:

    # calling the function sorted and passing args
    sort_me = sorted(samp_words, key=lambda w: w.lower())
    print(sort_me) # ['Abbey', 'arrow', 'BAss', 'BROWN', 'CACTUS', 'Crystal', 'DesTiny', 'dust', 'East', 'element', 'feet', 'Gag', 'Host', 'INVOKE', 'Jagger', 'JUMPER']
    rev_sort_me = sorted(samp_words, key=lambda w: w.lower(), reverse=True)
    print(rev_sort_me) # ['JUMPER', 'Jagger', 'INVOKE', 'Host', 'Gag', 'feet', 'element', 'East', 'dust', 'DesTiny', 'Crystal', 'CACTUS', 'BROWN', 'BAss', 'arrow', 'Abbey']

    # calling sort method of a type string
    samp_words.sort(key=str.lower) # apply the action on itself
    print(samp_words) # ['Abbey', 'arrow', 'BAss', 'BROWN', 'CACTUS', 'Crystal', 'DesTiny', 'dust', 'East', 'element', 'feet', 'Gag', 'Host', 'INVOKE', 'Jagger', 'JUMPER']
    samp_words.sort(key=str.lower, reverse=True)
    print(samp_words) # ['JUMPER', 'Jagger', 'INVOKE', 'Host', 'Gag', 'feet', 'element', 'East', 'dust', 'DesTiny', 'Crystal', 'CACTUS', 'BROWN', 'BAss', 'arrow', 'Abbey']


# set all values of the list lowercase and sort alphabetically in reverse order
sorted([word.lower() for word in samp_words], reverse=True)

# set all values of the list to lowercase and sort alphabetically based on the 2nd letter in reverse order
sorted([word.lower() for word in samp_words], key=lambda w: w[1], reverse=True)