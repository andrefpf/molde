from typing import Literal
from PyQt5.QtWidgets import QApplication
from molde import MOLDE_DIR


def get_stylesheet(theme=Literal["light", "dark"], *, extra_style=""):
    if theme == "light":
        qss_dir = MOLDE_DIR / "stylesheets/light"
    elif theme == "dark":
        qss_dir = MOLDE_DIR / "stylesheets/dark"
    else:
        return

    all_stylesheets = []
    for path in qss_dir.glob("*.qss"):
        all_stylesheets.append(path.read_text())
    all_stylesheets.append(extra_style)
    
    stylesheet = "\n\n".join(all_stylesheets)
    return stylesheet

def set_theme(theme=Literal["light", "dark"], *, extra_style=""):

    app: QApplication | None = QApplication.instance()
    if app is None:
        print("Ops")
        return

    stylesheet = get_stylesheet(theme)
    app.setStyleSheet(stylesheet)
