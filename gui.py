import time
import random
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtCore import QTimer, Qt
from logika import MenedzerWynikow

class GraReakcji(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gra na refleks")

        self.layout = QVBoxLayout()

        self.label = QLabel("Kliknij START i czekaj na zielone koło...")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.label)

        self.kolko = QLabel()
        self.kolko.setFixedSize(100, 100)
        self.kolko.setStyleSheet("background-color: gray; border-radius: 50px;")
        self.layout.addWidget(self.kolko)

        self.button = QPushButton("START")
        self.button.clicked.connect(self.start_game)
        self.layout.addWidget(self.button)

        self.wynik_label = QLabel("Top 10 wyników:")
        self.layout.addWidget(self.wynik_label)

        self.lista_label = QLabel()
        self.layout.addWidget(self.lista_label)

        self.setLayout(self.layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.zmien_na_zielone)

        self.wyniki = MenedzerWynikow()
        self.czekaj_na_klik = False
        self.start_time = 0
        self.klik_dozwolony = False

    def start_game(self):
        self.label.setText("Czekaj na zielone...")
        self.kolko.setStyleSheet("background-color: gray; border-radius: 50px;")
        self.button.setText("Czekaj...")
        self.button.setEnabled(True)
        self.czekaj_na_klik = False
        self.klik_dozwolony = False

        self.button.clicked.disconnect()
        self.button.clicked.connect(self.zbyt_wczesnie)

        opoznienie = random.randint(2000, 5000)
        self.timer.start(opoznienie)

    def zmien_na_zielone(self):
        self.timer.stop()
        self.kolko.setStyleSheet("background-color: green; border-radius: 50px;")
        self.label.setText("KLIKNIJ TERAZ!")
        self.button.setText("KLIKNIJ!")
        self.start_time = time.time()
        self.czekaj_na_klik = True
        self.klik_dozwolony = True

        self.button.clicked.disconnect()
        self.button.clicked.connect(self.zmierz_czas)

    def zbyt_wczesnie(self):
        if not self.klik_dozwolony:
            self.timer.stop()
            self.label.setText("Zbyt wcześnie!")
            self.kolko.setStyleSheet("background-color: gray; border-radius: 50px;")
            self.button.setText("START")
            self.button.clicked.disconnect()
            self.button.clicked.connect(self.start_game)

    def zmierz_czas(self):
        if self.czekaj_na_klik:
            czas = round((time.time() - self.start_time) * 1000)
            self.label.setText(f"Twój czas: {czas} ms")
            self.wyniki.dodaj_wynik(czas)
            self.aktualizuj_liste()
        else:
            self.label.setText("Zbyt wcześnie!")

        self.kolko.setStyleSheet("background-color: gray; border-radius: 50px;")
        self.button.setText("START")
        self.button.setEnabled(True)
        self.czekaj_na_klik = False
        self.klik_dozwolony = False
        self.button.clicked.disconnect()
        self.button.clicked.connect(self.start_game)

    def aktualizuj_liste(self):
        tekst = ""
        for i, wynik in enumerate(self.wyniki.pobierz_wyniki(), start=1):
            tekst += f"{i}. {wynik} ms\n"
        self.lista_label.setText(tekst)
