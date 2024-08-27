from typing import Literal
from PyQt5.QtWidgets import QApplication, QWidget
from molde import MOLDE_DIR


def set_qproperty(widget: QWidget, **kwargs):
    for key, val in kwargs.items():
        widget.setProperty(key, val)
    widget.style().polish(widget)

def get_variables(theme:Literal["light", "dark"] = "light") -> dict:
    variables = {
        "@border-radius": "5px",
    }

    if theme == "light":
        variables.update({
            "@primary-darker": "#0051A2",
            "@primary": "#0069D0",
            "@primary-lighter": "#007AF0",

            "@danger-color-darker": "#A4151E",
            "@danger-color": "#D01E29",
            "@danger-color-lighter": "#F02532",

            "@warning-color-darker": "#684F00",
            "@warning-color": "#866600",
            "@warning-color-lighter": "#9B7700",

            "@background": "#F0F0F5",
            "@background-variant": "#D3D4DD",
            "@on-background": "#000000",
            "@on-primary": "#FFFFFF",

            "@border-color": "#AAAAB9",
            "@input-color": "#F0F0F5",

            "@disabled-background": "#D3D4DD",
            "@disabled-color": "#a3a0a0",
        })

    elif theme == "dark":
        variables.update({
            "@primary-darker": "#007AF0",
            "@primary": "#498FFF",
            "@primary-lighter": "#84AAFF",

            "@danger-color-darker": "#A4151E",
            "@danger-color": "#D01E29",
            "@danger-color-lighter": "#F02532",

            "@warning-color-darker": "#684F00",
            "@warning-color": "#866600",
            "@warning-color-lighter": "#9B7700",

            "@background": "#24252E",
            "@background-variant": "#3A3A47",
            "@on-background": "#FFFFFF",
            "@on-primary": "#FFFFFF",

            "@border-color": "#515162",
            "@input-color": "#3A3A47",

            "@disabled-background": "#1c1d25",
            "@disabled-color": "#474646",
        })

    return variables

def get_stylesheet(theme:Literal["light", "dark"] = "light", *, extra_style=""):
    qss_dir = MOLDE_DIR / "stylesheets/"

    all_stylesheets = []
    for path in qss_dir.glob("*.qss"):
        all_stylesheets.append(path.read_text())
    all_stylesheets.append(extra_style)
    stylesheet = "\n\n".join(all_stylesheets)

    # Replace variables by correspondent data
    variable_size = lambda x: len(x[0])
    variables_mapping = sorted(get_variables(theme).items(), 
                               key=variable_size, reverse=True)
    for name, data in variables_mapping:
        stylesheet = stylesheet.replace(name, data)

    return stylesheet

def set_theme(theme=Literal["light", "dark"], *, extra_style=""):

    app: QApplication | None = QApplication.instance()
    if app is None:
        print("Ops")
        return

    stylesheet = get_stylesheet(theme)
    app.setStyleSheet(stylesheet)
