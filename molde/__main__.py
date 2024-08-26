import os, sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
from time import time

from molde import MOLDE_DIR
from molde import stylesheets


class Example(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        uic.loadUi(MOLDE_DIR / "stylesheets/example.ui", self)
        self.current_theme = "light"

        self.change_theme_button.clicked.connect(self.change_theme)

        self.show()

    
    def change_theme(self):
        if self.current_theme == "light":
            self.current_theme = "dark"
        else:
            self.current_theme = "light"
        
        stylesheets.set_theme(self.current_theme)

if __name__ == "__main__":
    # Make the window scale evenly for every monitor
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

    app = QApplication(sys.argv)
    stylesheets.set_theme("light")
    e = Example()
    sys.exit(app.exec())
