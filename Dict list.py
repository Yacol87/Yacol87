my_dict = { "1": "One",
            "2": "Two",
            "7": "Seven"
            }

print (my_dict.keys(), "My dict keys")
print (my_dict.values(), "My dict values")
print ("get my value for key  " + my_dict.get("7"))
print (my_dict.pop("2"))
print (my_dict)
my_dict.pop("1",1)
print (my_dict)