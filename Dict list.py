# my_dict = { "1": "One",
#             "2": "Two",
#             "7": "Seven"
#             }
#
# print (my_dict.keys(), "My dict keys")
# print (my_dict.values(), "My dict values")
# print ("get my value for key  " + my_dict.get("7"))
# print (my_dict.pop("2"))
# print (my_dict)
# my_dict.pop("1",1)
# print (my_dict)

check_number = input("Give me number, I will tell you divisors")
num2 = int(check_number)
list_of_divisors = []
x = 1
# print  (num2)
# print (num2*2)

while x < num2:
    if num2 % x == 0:
        list_of_divisors.append(x)
    x = x + 1


print(list_of_divisors)