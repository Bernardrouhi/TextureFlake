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

from ..core.obsoleteHelper import ProjectQObject

from .assetWidget import AssetTreeView, AssetItem, AssetModel
from .actionWidget import ActionWidget

from .dialogs.fileDialogs import SaveSceneDialog

class AssetLoaderWidget(QWidget):
	def __init__(self, project=ProjectQObject(), parent=None):
		super(AssetLoaderWidget, self).__init__(parent)

		self._project = project
		self._project.onWorkDirectoryUpdate.connect(self.reloadLocalWorkDirectory)

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

		workTitle_lb = QLabel(u"Path:")
		self.workDirectory_lb = QLabel(u"")

		layout.addWidget(workTitle_lb)
		layout.addWidget(self.workDirectory_lb)

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

		self.assetAction = ActionWidget()
		layout.addWidget(self.assetAction)

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

	def createNewAsset(self, button=bool):
		index = self.assets.currentIndex()
		item = self.assetModel.item(index.row(), index.column())
		# if item.parent() and not item.hasChildren():
		# 	print(item)
		
		# # check for open project
		# if SP.is_SceneOpen():
		# 	# check for changes in the current scene
		# 	if SP.is_NeedSaving():
		# 		dialog = SaveSceneDialog(title="Warning", message="The project hasn't been saved yet. Save the Scene?")
		# 		if dialog.exec_() == QDialog.Accepted:
		# 			SP.save_Scene()
		# 			SP.close_Scene()
		# 			SP.create_Scene()
		# 	else:
		# 		SP.close_Scene()
		# 		SP.create_Scene()
		# else:
		# 	SP.create_Scene()

	def exportTexture(self):
		print("Show Export Window")

	def selectedAsset(self, index=QModelIndex):
		item = self.assetModel.itemFromIndex(index)
		if item.parent() and not item.hasChildren():
			pass
		
	def loadAssets(self):
		self.assetModel.clear()
		assets = [
			{"Name":'Asset_01'},
			{"Name":'Asset_02'},
			{"Name":'Asset_03',}
		]
		for assetType in self._project.get_AssetTypesName():
			assteTypeItem = AssetItem({"Name":assetType})
			for asset in assets:
				nAsset = AssetItem(asset)
				assteTypeItem.appendRow(nAsset)
			self.assetModel.appendRow(assteTypeItem)

	def reloadLocalWorkDirectory(self):
		""" Update the widgets on local directory change.
		"""
		workDir = self._project.get_WorkDirectory()
		if os.path.exists(workDir):
			# Update Work Directory
			self.workDirectory_lb.setText(workDir)
			# Asset List
			self.assetAction.reload_ProjectInformation()
			# Asset Information
			self.loadAssets()
