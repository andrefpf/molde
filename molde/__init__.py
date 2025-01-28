from pathlib import Path
from qtpy.uic import loadUi
from .colors import Color
from PySide6.QtCore import QDir

MOLDE_DIR = Path(__file__).parent

def load_ui(uifile: str | Path, baseinstance, working_directory: str | Path = None):
    return loadUi(uifile, baseinstance, QDir(working_directory))