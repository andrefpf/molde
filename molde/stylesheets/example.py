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
        self.show()


if __name__ == "__main__":
    # Make the window scale evenly for every monitor
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

    app = QApplication(sys.argv)
    stylesheets.set_theme("light")
    e = Example()
    sys.exit(app.exec())
