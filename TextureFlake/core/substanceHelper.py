
import substance_painter.project
import substance_painter.ui
import os
from PySide2.QtWidgets import QMainWindow

def create_Scene():
	"""Create a new Substance Painter Project

	TODO replace HardCoded path to project based
	"""
	workFolder = os.path.abspath("D:/")
	meshFile = os.path.abspath(os.path.join(workFolder,"SKM_Sample_01.FBX"))
	templateFile = os.path.abspath(os.path.join(workFolder,"UnrealTemp.spt"))
	mySettings = substance_painter.project.Settings(
		import_cameras=False,
		normal_map_format=substance_painter.project.NormalMapFormat.DirectX)

	# create a scene
	substance_painter.project.create(
				mesh_file_path=meshFile,
				template_file_path=templateFile, 
				settings=mySettings)

	# save the scene to the file
	filePath = os.path.abspath(os.path.join(workFolder,"sample.spp"))
	saveAs_Scene(filePath)

def save_Scene():
	"""Save the current Substance Painter Project"""
	substance_painter.project.save(substance_painter.project.ProjectSaveMode.Full)

def get_FilePath():
	"""Get the current Substance Painter Project path.

		Returns: Path of current Substance Painter Project.
		Return Type: str
	"""
	return substance_painter.project.file_path()

def saveAs_Scene(filePath=str):
	"""Save the current Substance Painter Project into a new file
		
		Parameters:
		filePath (str) - Path of new File.
	"""
	substance_painter.project.save_as(filePath,substance_painter.project.ProjectSaveMode.Full)

def open_Scene(filePath=str):
	"""Open a Substance Painter Project
		
		Parameters:
		filePath (str) - Path to the .spp File.
	"""
	substance_painter.project.open(filePath) 

def close_Scene():
	"""Close the current Substance Painter Project"""
	substance_painter.project.close()

def is_SceneOpen():
	"""Check for if there is a active Substance Painter Project
		
		Returns: True if the any substance painter project is open, otherwise False.
		Return Type: bool
	"""
	return substance_painter.project.is_open()

def is_NeedSaving():
	"""Check for if there is any changes in the active Substance Painter Project
		
		Returns: True if there is any changes, otherwise False.
		Return Type: bool
	"""
	return substance_painter.project.needs_saving()

def add_MainWindow(widget=QMainWindow):
	"""Add a new QMainWindow to the Substance Painter application

		Parameters:
		widget (QMainWindow) - reference of the widget.
	"""
	substance_painter.ui.add_dock_widget(widget, 1)

def remove_MainWindow(widget=QMainWindow):
	"""Remove an existing QMainWindow from the Substance Painter application
		
		Parameters:
		widget (QMainWindow) - reference of the widget.
	"""
	substance_painter.ui.delete_ui_element(widget)

def get_SubstanceQMainWindow():
	"""Get the Substance Painter application QMainWindow
		
		Returns: Substance Painter QMainWindow Application.
		Return Type: <class 'PySide2.QtWidgets.QMainWindow'>
	"""
	return substance_painter.ui.get_main_window()