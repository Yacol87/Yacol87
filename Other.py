
diki = { "Jen" : "Wesoly moczymorda i leń, można pogadać i połazić po krzakach",
         "Mlo" : "Wyłysiały mądrala i gadula, mozna w wiele gier popykać",
         "Jar" : "Nieobecny hipokryta, można... W sumie pewnie nie przyjde",
         "Grz" : "poinformowany! Szwagier koleżanki z pracy siostry Magdy mi ostatnio opowiadał, że hamulce VXBC po 26 tygodniach.... "}


def give_relation():

    print ("Tacy ludzie są w pokoju " + str(list(diki.keys())))
    check_relation = input ("Z kim sprawdzić relację? ")
    print ("Kim jesteś " + check_relation)
    print ("Synek, ja jestem  " + diki[check_relation])
    wanna_check2 = input("Chcesz jeszcze sprawdzać?  Tak lub Nie ")
    if wanna_check2.upper() == ("TAK"):
        give_relation()
    else:
        print("no more checking")


wanna_check_relation = input("Czy chcesz sprawdzić kto jest w pokoju ?  Tak lub Nie ")

if wanna_check_relation in ("Tak","tak","t"):
     give_relation()
else: print("Juz nie sprawdzamy ")




