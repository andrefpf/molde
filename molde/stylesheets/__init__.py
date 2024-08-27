from typing import Literal
from PyQt5.QtWidgets import QApplication, QWidget
from molde import MOLDE_DIR
from molde.colors import Color, color_names


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
            "@primary-lighter": color_names.BLUE50.to_hex(),
            "@primary": color_names.BLUE40.to_hex(),
            "@primary-darker": color_names.BLUE30.to_hex(),

            "@danger-color-lighter": color_names.RED50.to_hex(),
            "@danger-color": color_names.RED40.to_hex(),
            "@danger-color-darker": color_names.RED30.to_hex(),

            "@warning-color-lighter": color_names.YELLOW50.to_hex(),
            "@warning-color": color_names.YELLOW40.to_hex(),
            "@warning-color-darker": color_names.YELLOW30.to_hex(),

            "@background": color_names.GRAY90.to_hex(),
            "@background-variant": color_names.GRAY80.to_hex(),

            "@on-primary": color_names.WHITE.to_hex(),
            "@on-background": color_names.BLACK.to_hex(),

            "@border-color": color_names.GRAY70.to_hex(),
            "@input-color": color_names.GRAY90.to_hex(),

            "@disabled-background": color_names.GRAY80.to_hex(),
            "@disabled-color": color_names.GRAY70.to_hex(),
        })

    elif theme == "dark":
        variables.update({
            "@primary-lighter": color_names.BLUE70.to_hex(),
            "@primary": color_names.BLUE60.to_hex(),
            "@primary-darker": color_names.BLUE50.to_hex(),

            "@danger-color-lighter": color_names.RED50.to_hex(),
            "@danger-color": color_names.RED40.to_hex(),
            "@danger-color-darker": color_names.RED30.to_hex(),

            "@warning-color-lighter": color_names.YELLOW50.to_hex(),
            "@warning-color": color_names.YELLOW40.to_hex(),
            "@warning-color-darker": color_names.YELLOW30.to_hex(),

            "@background": color_names.GRAY10.to_hex(),
            "@background-variant": color_names.GRAY20.to_hex(),

            "@on-background": color_names.WHITE.to_hex(),
            "@on-primary": color_names.WHITE.to_hex(),

            "@border-color": color_names.GRAY30.to_hex(),
            "@input-color": color_names.GRAY20.to_hex(),

            "@disabled-background": "#1c1d25",
            "@disabled-color": color_names.GRAY40.to_hex(),
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
