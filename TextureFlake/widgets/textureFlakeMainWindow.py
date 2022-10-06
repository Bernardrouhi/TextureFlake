import importlib, os
from PySide2.QtWidgets import (QMainWindow, QTabWidget, QDockWidget, QMenuBar,
								QAction, QFileDialog, QMenu, QDialog)
from PySide2.QtCore import Qt, QSettings, QStandardPaths

from . import projectLoaderWidget
importlib.reload(projectLoaderWidget)
from .dialogs import aboutDialog
importlib.reload(aboutDialog)


from Obsolete import envHandler as ObEnv
from ..core.obsoleteHelper import ProjectQObject
from .projectLoaderWidget import AssetLoaderWidget
from .dialogs.fileDialogs import SaveSettingsDialog
from .dialogs.aboutDialog import AboutDialog

# address %AppData%\Local\Allegorithmic\Substance Painter\TextureFlake
SETTINGS_PATH = f"{str(QStandardPaths.writableLocation(QStandardPaths.AppConfigLocation))}/TextureFlake"

class TextureFlakeMainWindow(QMainWindow):
	__version__ = "1.0.0"
	def __init__(self, parent=None):
		super(TextureFlakeMainWindow, self).__init__(parent)

		self.setWindowTitle(f'Texture Flake')
		self._project = ProjectQObject()

		self.setMinimumHeight(1)
		self.setMinimumWidth(1)

		# Asset Loader
		self.assetLoader = AssetLoaderWidget(project=self._project)
		self.setCentralWidget(self.assetLoader)

		# Menu
		self.setMenuBar(self.create_menu())

		self.init()

	def init(self):
		projectFile = ObEnv.check_project_env()
		self._project.load(ProjectFile=ObEnv.check_project_env())

	def create_menu(self):
		window_menu = QMenuBar(self)

		# Setup Menu
		setup_menu = window_menu.addMenu("&Setup")

		workfile_action = QAction("&Pick WorkDirectory", self)
		workfile_action.setStatusTip('Pick a local workdirectory to store the workfiles.')
		workfile_action.triggered.connect(self.setWorkDirectory)
		setup_menu.addAction(workfile_action)

		loadWork_action = QAction("&Load", self)
		loadWork_action.setStatusTip('Select from previous local work directory.')
		setup_menu.addAction(loadWork_action)
			
		self.load_menu = QMenu(self)
		self.update_LoadSettings()
		loadWork_action.setMenu(self.load_menu)

		# About menu
		about_menu = window_menu.addMenu("&About")
		about_action = QAction("&About TextureFlake...", self)
		about_action.setStatusTip('Information about plugin.')
		about_action.triggered.connect(self.about_plugin)
		about_menu.addAction(about_action)

		return window_menu

	def update_LoadSettings(self):
		self.load_menu.clear()
		self.load_menu.addActions(self.get_WorkDirecortyDistory(limit=20))

	def get_WorkDirecortyDistory(self, limit=int(5)):
		items = []
		for i in next(os.walk(SETTINGS_PATH), (None, None, []))[2]:
			fileName = f"{SETTINGS_PATH}/{i}"
			nSetting = QSettings(fileName, QSettings.IniFormat)
			nSetting.beginGroup("user")
			Name = nSetting.value("Name", "")
			nSetting.endGroup()
			
			# action Button
			history_action = QAction(f"&{Name}", self)
			history_action.setData(fileName)
			history_action.triggered.connect(self.onLoadSelected)
			
			items.append(history_action)
		return items

	def onLoadSelected(self, checked=bool):
		button = self.sender()
		filePath = button.data()
		if os.path.exists(filePath):
			nSetting = QSettings(filePath, QSettings.IniFormat)
			nSetting.beginGroup("user")
			workDir = nSetting.value(ObEnv.BaseENV.WORK_DIR, "")
			nSetting.endGroup()

			if os.path.exists(workDir):
				# set work directory, AssetLoaderWidget will auto update on WorkDirectory change
				self._project.set_WorkDirectory(work_directory=workDir)

	def setWorkDirectory(self):
		'''Pick Work Directory'''
		workDir = QFileDialog.getExistingDirectory(self, "Pick Work Directory Folder", os.path.expanduser("~"))
		if workDir:
			dialog = SaveSettingsDialog()
			if dialog.exec_() == QDialog.Accepted:
				FileName = dialog.getName()
				store = f"{SETTINGS_PATH}/{FileName}.ini"
				nSetting = QSettings(store, QSettings.IniFormat)
				nSetting.beginGroup("user")
				nSetting.setValue("Name", FileName)
				nSetting.setValue(ObEnv.BaseENV.WORK_DIR, workDir)
				nSetting.endGroup()
				nSetting.sync()

				# set work directory, AssetLoaderWidget will auto update on WorkDirectory change
				self._project.set_WorkDirectory(work_directory=workDir)
				# reload Load menu
				self.update_LoadSettings()
			else:
				print("-----Nothing Stored-----")

	def about_plugin(self):
		dialog = AboutDialog(version=self.__version__)
		dialog.exec_()