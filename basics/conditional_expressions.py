# long version
val = 4

if val % 2 == 0:
    val_out = f"{val} is an even number"
else:
    val_out = f"{val} is not an even number"

# short version
val_out = f"{val} is an even number" if val % 2 == 0 else f"{val} is not an even number"

print(val_out)

########## LAB ##########

name = input("What is your first name? ")

# 1) Call `print` with a different string using a single conditional expression
# if len(name) >= 6:
#     print(
#         "Your name is as long or longer than the average first name in the United States"
#     )
# else:
#     print("Your name is shorter than the average first name in the United States")

print("Your name is as long or longer than the average first name in the United States" if len(name)> 6 else "Your name is shorter than the average first name in the United States")

# 2) Set `message` using a single conditional expression
# if name[0].lower() in ["a", "j", "m", "e", "l"]:
#     message = "The first letter in your name is among the five most common"
# else:
#     message = "The first letter of your name is not among the five most common"

# print(message)

message = ("The first letter in your name is among the five most common" if name[0].lower() in ["a", "j", "m", "e", "l"] else "The first letter of your name is not among the five most common")
print(message)

# 3) Change the string passed to the `print` function using a conditional expression
# for letter in name:
#     if letter.lower() in ["a", "e", "i", "o", "u"]:
#         print(f"{letter} is a vowel")
#     else:
#         print(f"{letter} is a consonant")

for letter in name:
    print(f"{letter} is a vowel" if letter.lower() in ["a", "e", "i", "o", "u"] else f"{letter} is a consonant")


print("".join([f"{letter} is a vowel\n" if letter.lower() in ["a", "e", "i", "o", "u"] else f"{letter} is a consonant\n" for letter in name]))
