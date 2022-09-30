import importlib
from PySide2.QtWidgets import  (QWidget, QSizePolicy, QVBoxLayout, QHBoxLayout,
								QLabel, QPushButton, QDialog)
from PySide2.QtCore import Qt

from ..core import substanceHelper as SP
importlib.reload(SP)
from .dialogs import fileDialogs
importlib.reload(fileDialogs)

from .dialogs.fileDialogs import SaveSceneDialog

class AssetLoaderWidget(QWidget):
	def __init__(self, parent=None):
		super(AssetLoaderWidget, self).__init__(parent)

		self.setWindowTitle('Asset Loader')
		self.setMinimumSize(1,1)

		# ------------- Main Layout --------------
		main_layout = QVBoxLayout(self)
		main_layout.setContentsMargins(5,5,5,5)
		main_layout.setSpacing(5)
		main_layout.setAlignment(Qt.AlignTop)
		self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

		# ------- Row 1 -------
		# ----------------------------------------
		asset_layout = QHBoxLayout()
		asset_layout.setContentsMargins(0,0,0,0)
		asset_layout.setSpacing(5)
		asset_layout.setAlignment(Qt.AlignTop)

		main_layout.addLayout(asset_layout)

		asset_lb = QLabel(u"Asset Name:")
		asset_btn = QPushButton("New Scene")

		asset_layout.addWidget(asset_lb)
		asset_layout.addWidget(asset_btn)

		asset_btn.clicked.connect(self.createNewAsset)

	def createNewAsset(self, button=bool):
		if SP.is_SceneOpen():
			print("The project was successfully created.")
			if SP.is_NeedSaving():
				print("The project hasn't been saved yet.")
				dialog = SaveSceneDialog(title="Warning", message="The project hasn't been saved yet. Save the Scene?")
				if dialog.exec_() == QDialog.Accepted:
					SP.save_Scene()
					SP.close_Scene()
					SP.create_Scene()

			else:
				SP.close_Scene()
				SP.create_Scene()
		else:
			SP.create_Scene()
