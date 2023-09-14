# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# b = []
#
# for x in a:
#     if x < 5:
#         b.append(x)
#
# # print (b)
#
#
# # initializing list
# test_list = ['4', 'kg', 'butter', 'for', '40', 'bucks']
#
# # printing original list
# print("The original list : " + str(test_list))
#
# # using list comprehension + replace()
# # Replace substring in list of strings
# res = [sub.replace(test_list[2], 'replacement') for sub in test_list]
#
# # print result
# print("The list after substring replacement : " + str(res))
#
#
# x = lambda a, b, c : a + b * c
# print(x(5, 6, 2))
x=5
list22 = []
for i in range (0,x) :
    list22.append(i)
    if i == 3:
        list22.append(23)

print (list22)