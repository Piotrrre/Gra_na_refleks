class MenedzerWynikow:
    def __init__(self):
        self.najlepsze_wyniki = []

    def dodaj_wynik(self, czas):
        self.najlepsze_wyniki.append(czas)
        self.najlepsze_wyniki.sort()
        self.najlepsze_wyniki = self.najlepsze_wyniki[:10]

    def pobierz_wyniki(self):
        return self.najlepsze_wyniki
