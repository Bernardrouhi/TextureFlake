import importlib, os
from PySide2.QtWidgets import  (QWidget, QSizePolicy, QVBoxLayout, QHBoxLayout,
								QLabel, QLineEdit, QPushButton, QDialog, QComboBox,
								QFileDialog)
from PySide2.QtCore import Qt, QModelIndex

from ..core import obsoleteHelper as Ob
importlib.reload(Ob)
from ..core import substanceHelper as SP
importlib.reload(SP)
from .dialogs import fileDialogs
importlib.reload(fileDialogs)
from . import assetWidget
importlib.reload(assetWidget)
from . import actionWidget
importlib.reload(actionWidget)
from Obsolete import envHandler as ObEnv

from .assetWidget import AssetTreeView, AssetItem, AssetModel
from .actionWidget import ActionWidget

from .dialogs.fileDialogs import SaveSceneDialog

class AssetLoaderWidget(QWidget):
	def __init__(self, parent=None):
		super(AssetLoaderWidget, self).__init__(parent)

		self._project = Ob.ProjectQObject(ProjectFile=ObEnv.check_project_env())
		self._project.onWorkDirectoryUpdate.connect(self.changeHappen)

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
		layout = QHBoxLayout()
		layout.setContentsMargins(0,0,0,0)
		layout.setSpacing(5)
		layout.setAlignment(Qt.AlignTop)

		main_layout.addLayout(layout)

		work_btn = QPushButton("Pick Workdirectory")
		layout.addWidget(work_btn)

		work_btn.clicked.connect(self.pick_Workdirectory)

		layout.addWidget(work_btn)

		# ------- Row 2 -------
		# ----------------------------------------
		layout = QHBoxLayout()
		layout.setContentsMargins(0,0,0,0)
		layout.setSpacing(5)
		layout.setAlignment(Qt.AlignTop)

		main_layout.addLayout(layout)

		assetSearch_lb = QLabel(u"Search:")

		self.assetsearch_in = QLineEdit()

		layout.addWidget(assetSearch_lb)
		layout.addWidget(self.assetsearch_in)

		# ------- Row 3 -------
		# ----------------------------------------
		layout = QHBoxLayout()
		layout.setContentsMargins(0,0,0,0)
		layout.setSpacing(5)
		layout.setAlignment(Qt.AlignTop)

		main_layout.addLayout(layout)

		self.assets = AssetTreeView()
		self.assets.clicked.connect(self.selectedAsset)

		self.assetModel = AssetModel()
		self.assets.setModel(self.assetModel)

		layout.addWidget(self.assets)

		# ------- Row 4 -------
		# ----------------------------------------
		layout = QHBoxLayout()
		layout.setContentsMargins(0,0,0,0)
		layout.setSpacing(5)
		layout.setAlignment(Qt.AlignTop)

		main_layout.addLayout(layout)

		action = ActionWidget()
		layout.addWidget(action)

		# ------- Row 5 -------
		# ----------------------------------------
		layout = QHBoxLayout()
		layout.setContentsMargins(0,0,0,0)
		layout.setSpacing(5)
		layout.setAlignment(Qt.AlignTop)

		main_layout.addLayout(layout)

		asset_btn = QPushButton("Test Create Scene")
		layout.addWidget(asset_btn)

		asset_btn.clicked.connect(self.createNewAsset)

		# ------- Row 6 -------
		# ----------------------------------------
		layout = QHBoxLayout()
		layout.setContentsMargins(0,0,0,0)
		layout.setSpacing(5)
		layout.setAlignment(Qt.AlignTop)

		main_layout.addLayout(layout)

		export_btn = QPushButton("Export Textures")
		layout.addWidget(export_btn)

		export_btn.clicked.connect(self.exportTexture)

		self.loadAssets()

	def pick_Workdirectory(self):
		work_Dir = QFileDialog.getExistingDirectory(self,"Pick Work Directory Folder", os.path.expanduser("~"))
		if work_Dir:
			self._project.set_WorkDirectory(work_directory=work_Dir)

	def createNewAsset(self, button=bool):
		# check for open project
		if SP.is_SceneOpen():
			# check for changes in the current scene
			if SP.is_NeedSaving():
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

	def exportTexture(self):
		print("Show Export Window")

	def selectedAsset(self, index=QModelIndex):
		item = self.assetModel.itemFromIndex(index)
		
	def loadAssets(self):
		assets = [
			{"Name":'Asset_01'},
			{"Name":'Asset_02'},
			{"Name":'Asset_03',}
		]
		for assetType in self._project.get_AssetTypesName():
			assteTypeItem = AssetItem({"Name":assetType})
			# for asset in assets:
			# 	nAsset = AssetItem(asset)
			# 	assteTypeItem.appendRow(nAsset)
			self.assetModel.appendRow(assteTypeItem)

	def changeHappen(self):
		print("ChangeHappen")