from PySide2.QtWidgets import  (QWidget, QSizePolicy, QVBoxLayout, QHBoxLayout,
								QLabel, QLineEdit, QPushButton, QDialog, QComboBox,
								QFileDialog)
from PySide2.QtCore import Qt, QModelIndex

class ActionWidget(QWidget):
	def __init__(self, parent=None):
		super(ActionWidget, self).__init__(parent)

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


