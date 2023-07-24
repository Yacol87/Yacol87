def convert_time_to_seconds():
    print ("We will ocnvert time into seconds")
    hour = float(input ("Type current hour"))
    minutes = float(input ("type current minute"))
    listaa = [hour, minutes]

    print (listaa)
    if type(hour) is float and type(minutes) is float:
        print("cool, we got numbers")
    else:
        print("we need numbers to do this, won't work with strings")

    seconds = float(minutes*60 + hour*3600)
    print("That many seconds elapsed today: " , seconds)

convert_hour = input("Do you wana convert some hours? Say Yes or No")

if convert_hour == "Yes":
    convert_time_to_seconds()
else:
    print("You dont wanna convert hous :/")
