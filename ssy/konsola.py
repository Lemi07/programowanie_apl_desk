class Osoba: 
    instancje = 0
    def __init__(self, id: int=0, imie: str =""):
        self.__id=id
        self.__imie=imie
        Osoba.instancje +=1
    def kopiuj(self, osoba: "Osoba"):
        self.__id = osoba.__id
        self.__imie = osoba.__imie
        
    def witaj(self, imie: str):
        
        if not self.__imie:
            print("brak danych")
        else:
            print(f"Cześć {imie}, mam na imię {self.__imie} ")
       
print(f"\nliczba zarejestrowanych osób: {Osoba.instancje}")      
            
osoba1 = Osoba()

wypisane_id=int(input("Podaj id: "))
wypisane_imie=input("Podaj imię: ")
osoba2 = Osoba(wypisane_id, wypisane_imie)
osoba2.witaj("Jan")

osoba3 = Osoba()
osoba3.kopiuj(osoba2)
osoba2.witaj("Jan")

print(f"\nliczba zarejestrowanych osób: {Osoba.instancje}")