import importlib
from PySide2.QtWidgets import (QDialog, QVBoxLayout, QPushButton, QLabel)
from PySide2.QtCore import Qt

class AboutDialog(QDialog):
	def __init__(self, version=str(), parent=None, **kwargs):
		QDialog.__init__(self, **kwargs)

		self.setWindowTitle("About TextureFlake")
		self.setWindowFlags(Qt.WindowStaysOnTopHint)
		self.resize(500, 500)

		# ------------- Main Layout --------------
		mainLayout = QVBoxLayout(self)
		mainLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
		self.setLayout(mainLayout)

		# ------- Row 1 -------
		# ----------------------------------------
		app_lb = QLabel(f"TextureFlake")
		version_lb = QLabel(f"Version v{version}")
		
		mainLayout.addWidget(app_lb)
		mainLayout.addWidget(version_lb)

		# ------- Row 2 -------
		# ----------------------------------------
		ok_btn = QPushButton("ok")
		ok_btn.clicked.connect(self.accept)

		mainLayout.addWidget(ok_btn)
