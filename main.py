import sys
from PyQt6.QtWidgets import QApplication
from gui import GraReakcji

if __name__ == "__main__":
    app = QApplication(sys.argv)
    okno = GraReakcji()
    okno.show()
    sys.exit(app.exec())
