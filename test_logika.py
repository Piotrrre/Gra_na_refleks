import unittest
from logika import MenedzerWynikow

class TestMenedzerWynikow(unittest.TestCase):
    def test_dodaj_wynik_sortowanie(self):
        m = MenedzerWynikow()
        m.dodaj_wynik(350)
        m.dodaj_wynik(150)
        m.dodaj_wynik(250)
        self.assertEqual(m.pobierz_wyniki(), [150, 250, 350])

    def test_dodaj_wynik_ograniczenie_do_10(self):
        m = MenedzerWynikow()
        for i in range(20, 0, -1):  # dodaj 20 wyników od 200 do 10
            m.dodaj_wynik(i * 10)
        wyniki = m.pobierz_wyniki()
        self.assertEqual(len(wyniki), 10)
        self.assertEqual(wyniki, [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

if __name__ == "__main__":
    unittest.main()
