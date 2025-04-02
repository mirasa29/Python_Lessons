# Closures are functions that return a function

def greeter(prefix):
    def greet(name):
        print(f"{prefix} {name}")
    return greet


hello = greeter('Hello,')
bye = greeter('Goodbye,')
aussie_greet = greeter("G'day,")

hello('Kevin')
bye('Kyle')
aussie_greet('James')


# class Tao:
#     def __init__(self, name):
#         self.name = name
#
#     def show_name(self):
#         return f'Tao: {self.name}'
#
# person1 = Tao('Jose')
# print(person1.name)
# print(person1.show_name())