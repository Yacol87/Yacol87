
diki = { "Jen" : "Wesoly moczymorda i leń, można pogadać i połazić",
         "Mlo" : "Wyłysiały mądrala i gadula, mozna w wiele gier popykać",
         "Jar" : "Nieobecny hipokryta, można... W sumie pewnie nie przyjdzie"}


def give_relation():

    print ("Following people are in the room: " + str(list(diki.keys())))
    check_relation = input ("With whom would you like to check relation? ")
    print ("Who are you " + check_relation)
    print ("I am your  " + diki[check_relation])
    wanna_check2 = input("do you want to check more relations? Say Yes or No ")
    if wanna_check2 in ("Yes","yes"):
        give_relation()
    else:
        print("no more checking")


wanna_check_relation = input("Want to check relation with someone? Yes or No ")


if wanna_check_relation in ("Yes","yes","y"):
     give_relation()
else: print("I guess no checking today ")

