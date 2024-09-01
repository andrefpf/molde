import os, sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from time import time

from molde import MOLDE_DIR
from molde import stylesheets
from molde.render_widgets.common_render_widget import CommonRenderWidget


class Example(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        uic.loadUi(MOLDE_DIR / "stylesheets/mainwindow.ui", self)
        self.current_theme = "light"

        self.change_theme_button.clicked.connect(self.change_theme)
        self.render_widget: CommonRenderWidget
        self.render_widget.create_axes()
        self.render_widget.create_scale_bar()
        self.render_widget.create_color_bar()
        self.render_widget.set_info_text("Hola\nque\ntal?")
        self.show()

    
    def change_theme(self):
        if self.current_theme == "light":
            self.current_theme = "dark"
        else:
            self.current_theme = "light"
        
        self.render_widget.set_theme(self.current_theme)
        stylesheets.set_theme(self.current_theme)

if __name__ == "__main__":
    # Make the window scale evenly for every monitor
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

    app = QApplication(sys.argv)
    e = Example()
    e.change_theme()
    sys.exit(app.exec())
