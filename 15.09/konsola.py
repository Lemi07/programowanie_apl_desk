class sortowanie:
    def __init__(self):
        self.tablica=[]
    def wczytaj(self):
        print("Podaj 10 liczb do tablicy")
        for i in range(10):
            liczba = int(input(f"Podaj element {i+1} tablicy: "))
            self.tablica.append(liczba)
#/********************************************************
#* nazwa funkcji: najwyzsza
#* parametry wejściowe: brak
#* wartość zwracana: n - najwyższa wartość liczbowa znaleziona w tablicy
#* autor: LTomys
#****************************************************/
    def najwyzsza(self):
        n=self.tablica[0]
        for i in self.tablica:
            if i>n:
                n=i
        return n
#/********************************************************
#* nazwa funkcji: sortuj
#* parametry wejściowe: brak
#* wartość zwracana: self.tablica - tablica posortowana malejąco
#* autor: LTomys
#****************************************************/    
    def sortuj(self):
        posortowana = []
        while len(self.tablica)>0:
            max =self.najwyzsza()
            posortowana.append(max)
            self.tablica.remove(max)
        self.tablica=posortowana
        return self.tablica
            
            
sortujWybieranie = sortowanie()
sortujWybieranie.wczytaj()
sortujWybieranie.najwyzsza()
print(sortujWybieranie.sortuj())
        
