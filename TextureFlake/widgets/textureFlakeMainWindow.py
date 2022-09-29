import importlib
from PySide2.QtWidgets import (QMainWindow, QTabWidget, QDockWidget)
from PySide2.QtCore import Qt

from . import projectLoaderWidget
importlib.reload(projectLoaderWidget)

from .projectLoaderWidget import AssetLoaderWidget

class TextureFlakeMainWindow(QMainWindow):
	def __init__(self, parent=None):
		super(TextureFlakeMainWindow, self).__init__(parent)
		self.__version__ = "1.0"

		self.setWindowTitle(f'Texture Flake v{self.__version__}')

		self.setMinimumHeight(1)
		self.setMinimumWidth(1)

		# Asset Loader
		self.assetLoader = AssetLoaderWidget()
		self.setCentralWidget(self.assetLoader)
