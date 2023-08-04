# DICTIONARY
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




#LISTS
fruit_list = ["apple", "banana", "cherry","plum"]
number_list = [1, 5, 7, 9, 11, 13]
boolean_list = [True, False, False]

print(fruit_list, number_list, boolean_list)

x1 = 11
x2= 0
while x1 < 20:
    print(number_list[x2], fruit_list[x2], "\n")
    x1 += 3
    x2 +=1
    # print(x1)

print("List of lists with If, daaaaum \n")

list_of_lists = [[[l2 for l2 in range(3)] for l3 in range(4)] for l4 in range (5)]

print(list_of_lists)


# for x in fruit_list:
#     print(x)