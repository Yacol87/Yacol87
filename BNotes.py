PERSONAL NOTES AND Way of doing things
SETUP
# Settings - Ctrl + Alt + 0
# Git
#

#
CODING
# Comment all - Ctrl + /
# Shift Shift - search everywhere
# F2 - jump between issues
# Ctrl + W - extend selection

LISTS
# List               /Set	           /Tuple
# Mutable	         /Mutable	       /Immutable
# Ordered  	         /Unordered        /Ordered
# Can change items   /Cannot change    /Can change items
# Can duplicate      /Cannot Duplic    /Can duplicate
#
# print (list[3:]) - display items after 3rd onwards
# COMPARE LSITS AND PRINT SEPECIFIC ITEMS
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = []
# for x in a:
#     if x < 5:
#         b.append(x)
# print (b)

CLASSES
#
# dump function - shows attributes with values and methods that this object has
#def dump(jan):
#   for attr in dir(jan):
#     print("jan.%s = %r" % (attr, getattr(jan, attr)))
#
# dump(jan)
# jan.__class__ = <class '__main__.Kid'>
# jan.__delattr__ = <method-wrapper '__delattr__' of Kid object at 0x0000025F42BA0FD0>
# jan.__dict__ = {'imie': 'Jan', 'wiek': 9}
# jan.__dir__ = <built-in method __dir__ of Kid object at 0x0000025F42BA0FD0>
# jan.__doc__ = None
# jan.__eq__ = <method-wrapper '__eq__' of Kid object at 0x0000025F42BA0FD0>
# jan.__format__ = <built-in method __format__ of Kid object at 0x0000025F42BA0FD0>
# jan.__ge__ = <method-wrapper '__ge__' of Kid object at 0x0000025F42BA0FD0>
# jan.__getattribute__ = <method-wrapper '__getattribute__' of Kid object at 0x0000025F42BA0FD0>
# jan.__gt__ = <method-wrapper '__gt__' of Kid object at 0x0000025F42BA0FD0>
# jan.__hash__ = <method-wrapper '__hash__' of Kid object at 0x0000025F42BA0FD0>
# jan.__init__ = <bound method Kid.__init__ of <__main__.Kid object at 0x0000025F42BA0FD0>>
# jan.__init_subclass__ = <built-in method __init_subclass__ of type object at 0x0000025F42A5BA80>
# jan.__le__ = <method-wrapper '__le__' of Kid object at 0x0000025F42BA0FD0>
# jan.__lt__ = <method-wrapper '__lt__' of Kid object at 0x0000025F42BA0FD0>
# jan.__module__ = '__main__'
# jan.__ne__ = <method-wrapper '__ne__' of Kid object at 0x0000025F42BA0FD0>
# jan.__new__ = <built-in method __new__ of type object at 0x00007FFC97A14E00>
# jan.__reduce__ = <built-in method __reduce__ of Kid object at 0x0000025F42BA0FD0>
# jan.__reduce_ex__ = <built-in method __reduce_ex__ of Kid object at 0x0000025F42BA0FD0>
# jan.__repr__ = <method-wrapper '__repr__' of Kid object at 0x0000025F42BA0FD0>
# jan.__setattr__ = <method-wrapper '__setattr__' of Kid object at 0x0000025F42BA0FD0>
# jan.__sizeof__ = <built-in method __sizeof__ of Kid object at 0x0000025F42BA0FD0>
# jan.__str__ = <method-wrapper '__str__' of Kid object at 0x0000025F42BA0FD0>
# jan.__subclasshook__ = <built-in method __subclasshook__ of type object at 0x0000025F42A5BA80>
# jan.__weakref__ = None


FILES
# "x" - Create - will create a file, returns an error if the file exist
# "a" - Append - will create a file if the specified file does not exist
# "w" - Write - will create a file if the specified file does not exist
# "r" - read from the file
# contentUsera = input("Co chcesz dopisać do pliku ")
# f = open("D:\down\myfile.txt", "w")
# f.write("\n" + contentUsera)