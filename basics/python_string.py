sample_string = 'To the Moon and back'

# -- LENGTH --  #

# print the length of the string using len function
print(len(sample_string)) # result is 18

# print the length of the string using __len__ method
print(sample_string.__len__())

# -- INDEXING --  #

# print all characters in the string
print(sample_string)  # result is 'To the Moon and back'

# print the first character in the string using indexing
print(sample_string[0])  # result is T

# print the last character in the string using indexing
print(sample_string[-1])  # result is k

# -- SORTING --  #

# sort the string in ascending order
print(''.join(sorted(sample_string, key=lambda l: l.lower())))  # result is '    aabcdehkMnnoooTt'

# print string in reverse
print(sample_string[::-1]) # result is 'kcab dna nooM eht oT'

# reversing the case of the string
print(sample_string.swapcase())  # result is 'tO THE mOON AND BACK'


# -- SLICING --  #

# print all characters in the string using slicing
print(sample_string[:])  # result is 'To the Moon and back'

# print all characters in the string using slicing
print(sample_string[0:20])  # result is 'To the Moon and back' (note: 20 is the length of the string)

# print the last character of the string using slicing
print(sample_string[-1:])  # result is 'k'

# print the first 3 characters in the string using slicing
print(sample_string[:3])  # result is 'To '

# print the last 3 characters in the string using slicing
print(sample_string[-3:])  # result is 'ack'

# print from start to the 3rd to the last character in the string using slicing
print(sample_string[:-3])  # result is 'To the Moon and b'

# check if the string contains 'm'
sample_string.__contains__('M')  # True

# output string replacing the spaces with no space
samp_str.replace(' ', '')  # 'TotheMoonandback' note: this does not change the original string

# output string stripping the spaces (leading and trailing) and prefix and suffix
sample_string = '   ' + sample_string + '   '  # adding spaces to the beginning and end of the string
sample_string.strip()  # result is 'To the Moon and back'
sample_string.rstrip()  # result is '   To the Moon and back'
sample_string.lstrip()  # result is 'To the Moon and back   '
sample_string = 'prefix' + sample_string + 'suffix'  # adding prefix and suffix to the string
sample_string.removeprefix('prefix')  # result is '   To the Moon and back   suffix'
sample_string.removesuffix('suffix')  # result is '   To the Moon and back   '

# resetting the sample_string
sample_string = 'To the Moon and back'

# get the index of a character in the right-most position
sample_string.rindex('o')  # result is 9
sample_string.rfind('o')  # result is 9

# get the index of a character in the left-most position
sample_string.index('o')  # result is 1
sample_string.find('o')  # result is 1

# check if the string starts with 'T'
sample_string.startswith('T')  # True
sample_string.startswith('t')  # False

# check if the string ends with 'k'
sample_string.endswith('k')  # True

# use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}

txt = "Hello Sam!"

print(txt.translate(mydict))  # result is 'Hello Pam!'




###################################
# Potential Interview Question

# Given a string, write a function that returns the string with all vowels removed.
# For example, the string "Hello, World!" would become "Hll, Wrld!".
# Note: the function should remove all vowels, including "y" if it is not at the start of a word.
###################################


def remove_vowels(s):
    return ''.join([i for i in s if i.lower() not in 'aeiou'])


print(remove_vowels("Hello, World!"))  # Hll, Wrld!

