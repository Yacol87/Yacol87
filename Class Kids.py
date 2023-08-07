class Kid:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek
        print(imie,"ma już", wiek, "lat")

    def podaj_imie(self):
        return self.imie
    def podaj_wiek(self):
        return self.wiek


    def ask(self):
        print("Tataaa, a co toooo?")

jan = Kid("Jan",9)
alicja = Kid("Alicja",7)
julia = Kid("Julia",5)


lista_dzieci = []


lista_dzieci.append(jan.imie)
lista_dzieci.append(alicja.__dict__)
lista_dzieci.append(julia.__dict__)

print (lista_dzieci)
print(type(jan))