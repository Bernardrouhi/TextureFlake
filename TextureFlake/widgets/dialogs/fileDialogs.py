import importlib
from PySide2.QtWidgets import (QDialog, QGridLayout, QPushButton, QLabel, QLineEdit)
from PySide2.QtGui import QRegExpValidator
from PySide2.QtCore import Qt, QRegExp

from ...core import substanceHelper as SP
importlib.reload(SP)

class SaveSceneDialog(QDialog):
	def __init__(self, title=str, message=str, parent=None):
		super(SaveSceneDialog, self).__init__(parent=parent)

		# ------------- Main Layout --------------
		mainLayout = QGridLayout(self)
		mainLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
		mainLayout.setColumnStretch(0,0)
		mainLayout.setColumnStretch(1,1)
		mainLayout.setColumnStretch(2,1)
		mainLayout.setColumnStretch(3,1)
		self.setLayout(mainLayout)

		# ------- Row 1 -------
		# ----------------------------------------
		message_lb = QLabel(message)
		message_lb.setAlignment(Qt.AlignRight)
		mainLayout.addWidget(message_lb, 0, 0)

		# ------- Row 2 -------
		# ----------------------------------------
		save_btn = QPushButton("Save")
		save_btn.clicked.connect(self.accept)
		cancel_btn = QPushButton("Cancel")
		cancel_btn.clicked.connect(self.reject)

		mainLayout.addWidget(save_btn, 1, 1, 1, 1)
		mainLayout.addWidget(cancel_btn, 1, 3, 1, 1)
		self.setWindowTitle(title)
		self.setWindowFlags(Qt.WindowStaysOnTopHint)

class SaveSettingsDialog(QDialog):
	def __init__(self, parent=None):
		QDialog.__init__(self)

		# ------------- Main Layout --------------
		mainLayout = QGridLayout(self)
		mainLayout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
		mainLayout.setColumnStretch(0,0)
		mainLayout.setColumnStretch(1,1)
		mainLayout.setColumnStretch(2,1)
		mainLayout.setColumnStretch(3,1)
		self.setLayout(mainLayout)

		# ------- Row 1 -------
		# ----------------------------------------
		message_lb = QLabel("Give a name to the setting")
		message_lb.setAlignment(Qt.AlignRight)
		mainLayout.addWidget(message_lb, 0, 0)

		# ------- Row 2 -------
		# ----------------------------------------
		self.name_in = QLineEdit()
		self.name_in.setValidator(QRegExpValidator(QRegExp("[a-z-A-Z_]+")))
		mainLayout.addWidget(self.name_in, 1, 0)

		# ------- Row 3 -------
		# ----------------------------------------
		save_btn = QPushButton("Save")
		save_btn.clicked.connect(self.accept)
		cancel_btn = QPushButton("Cancel")
		cancel_btn.clicked.connect(self.reject)

		mainLayout.addWidget(save_btn, 2, 1, 1, 1)
		mainLayout.addWidget(cancel_btn, 2, 3, 1, 1)
		self.setWindowTitle("Create a new Setting")
		self.setWindowFlags(Qt.WindowStaysOnTopHint)

	def getName(self):
		return self.name_in.text()
