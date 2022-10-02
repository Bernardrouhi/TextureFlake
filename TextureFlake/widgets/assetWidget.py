from PySide2.QtWidgets import QListView, QTreeView, QAbstractItemView, QMenu, QAction
from PySide2.QtGui import QStandardItem, QStandardItemModel
from PySide2.QtCore import Qt, QPoint

class AssetTreeView(QTreeView):
	def __init__(self):
		super(AssetTreeView, self).__init__()

		self.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.setContextMenuPolicy(Qt.CustomContextMenu)
		self.customContextMenuRequested.connect(self.assetMenu)
		self.setHeaderHidden(True)

	def assetMenu(self, point=QPoint):
		self.assetTMenu = QMenu()

		# New Asset
		new_action = QAction("Create Asset", self)
		new_action.setStatusTip('Create a new Asset in workspace.')
		new_action.triggered.connect(self.show_AssetCreationDialog)
		self.assetTMenu.addAction(new_action)

		self.assetTMenu.addSeparator()

		self.assetTMenu.move(self.viewport().mapToGlobal(point))
		self.assetTMenu.show()

	def show_AssetCreationDialog(self):
		pass

class AssetItem(QStandardItem):
	def __init__(self, model=dict):
		self._localData = model
		super(AssetItem, self).__init__(model["Name"])

	def getAssetVersions(self):
		return 

class AssetModel(QStandardItemModel):
	def __init__(self, *args, **kwargs):
		super(AssetModel, self).__init__(*args, **kwargs)
