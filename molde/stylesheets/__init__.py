from typing import Literal
from PyQt5.QtWidgets import QApplication
from molde import MOLDE_DIR


def get_variables(theme:Literal["light", "dark"] = "light") -> dict:
    variables = {
        "@border-radius": "5px",
    }

    if theme == "light":
        variables.update({
            "@primary": "#0069D0",
            "@primary-darker": "#0051A2",
            "@primary-lighter": "#007AF0",
            "@background": "#F0F0F5",
            "@background-variant": "#F0F0F5",
            "@on-background": "#000000",
            "@on-primary": "#FFFFFF",
        })

    elif theme == "dark":
        variables.update({
            "@primary": "#0069D0",
            "@primary-darker": "#0051A2",
            "@primary-lighter": "#007AF0",

            "@background": "#000000",
            "@background-variant": "#F0F0F5",
            "@on-background": "#FFFFFF",
            "@on-primary": "#FFFFFF",
        })

    return variables

def get_stylesheet(theme:Literal["light", "dark"] = "light", *, extra_style=""):
    qss_dir = MOLDE_DIR / "stylesheets/light"

    if theme == "dark":
        return ""

    all_stylesheets = []
    for path in qss_dir.glob("*.qss"):
        all_stylesheets.append(path.read_text())
    all_stylesheets.append(extra_style)
    stylesheet = "\n\n".join(all_stylesheets)

    # Replace variables by correspondent data
    for name, data in get_variables(theme).items():
        stylesheet = stylesheet.replace(name, data)

    return stylesheet

def set_theme(theme=Literal["light", "dark"], *, extra_style=""):

    app: QApplication | None = QApplication.instance()
    if app is None:
        print("Ops")
        return

    stylesheet = get_stylesheet(theme)
    app.setStyleSheet(stylesheet)
