from PySide2.QtWidgets import  (QWidget, QSizePolicy, QVBoxLayout, QHBoxLayout,
								QLabel, QLineEdit, QPushButton, QDialog, QComboBox,
								QFileDialog)
from PySide2.QtCore import Qt, QModelIndex

from Obsolete import pipelineNode as ObPipe

class ActionWidget(QWidget):
	def __init__(self, parent=None):
		super(ActionWidget, self).__init__(parent)

		self._pipeline = ObPipe.Pipeline()
		self.setWindowTitle('Asset')
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

		projectNameTitle_lb = QLabel(u"Project:")
		self.projectName_lb = QLabel(u"")

		layout.addWidget(projectNameTitle_lb)
		layout.addWidget(self.projectName_lb)

		# ------- Row 2 -------
		# ----------------------------------------
		layout = QHBoxLayout()
		layout.setContentsMargins(0,0,0,0)
		layout.setSpacing(5)
		layout.setAlignment(Qt.AlignTop)

		main_layout.addLayout(layout)

		assetTypeTitle_lb = QLabel(u"AssetType:")
		self.assetType_lb = QLabel(u"")

		layout.addWidget(assetTypeTitle_lb)
		layout.addWidget(self.assetType_lb)

		# ------- Row 3 -------
		# ----------------------------------------
		layout = QHBoxLayout()
		layout.setContentsMargins(0,0,0,0)
		layout.setSpacing(5)
		layout.setAlignment(Qt.AlignTop)

		main_layout.addLayout(layout)

		assetContainerTitle_lb = QLabel(u"AssetContainer:")
		self.assetContainer_lb = QLabel(u"")

		layout.addWidget(assetContainerTitle_lb)
		layout.addWidget(self.assetContainer_lb)

		# ------- Row 3 -------
		# ----------------------------------------
		layout = QHBoxLayout()
		layout.setContentsMargins(0,0,0,0)
		layout.setSpacing(5)
		layout.setAlignment(Qt.AlignTop)

		main_layout.addLayout(layout)

		assetNameTitle_lb = QLabel(u"AssetName:")
		self.assetName_lb = QLabel(u"")

		layout.addWidget(assetNameTitle_lb)
		layout.addWidget(self.assetName_lb)

	def reload_ProjectInformation(self):
		self.set_ProjectName()
		self.set_AssetType()
		self.set_AssetContainer()
		self.set_AssetName()

	def set_ProjectName(self):
		projectName = self._pipeline.get_ProjectName()
		if projectName : self.projectName_lb.setText(projectName)

	def set_AssetType(self):
		assetType = self._pipeline.get_AssetType()
		if assetType : self.assetType_lb.setText(assetType)

	def set_AssetContainer(self):
		assetContainer = self._pipeline.get_AssetContainer()
		if assetContainer : self.assetContainer_lb.setText(assetContainer)

	def set_AssetName(self):
		assetName = self._pipeline.get_AssetName()
		if assetName : self.assetName_lb.setText(assetName)


