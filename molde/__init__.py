from pathlib import Path
from qtpy.uic import loadUi
from .colors import Color

MOLDE_DIR = Path(__file__).parent

def load_ui(uifile, baseinstance, working_directory=None):
    return loadUi(uifile, baseinstance, working_directory)