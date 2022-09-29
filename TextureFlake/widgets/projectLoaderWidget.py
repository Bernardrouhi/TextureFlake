from PySide2.QtWidgets import  (QWidget, QSizePolicy, QVBoxLayout, QHBoxLayout,
								QLabel, QComboBox)
from PySide2.QtCore import Qt

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

		asset_layout.addWidget(asset_lb)
