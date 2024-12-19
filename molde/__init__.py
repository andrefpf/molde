from pathlib import Path
from qtpy.uic import loadUi
from .colors import Color

MOLDE_DIR = Path(__file__).parent

def load_ui(uifile, baseinstance):
    return loadUi(uifile, baseinstance)