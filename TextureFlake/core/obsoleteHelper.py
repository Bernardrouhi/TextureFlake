import importlib
from PySide2.QtCore import (Signal, QObject)

import Obsolete
importlib.reload(Obsolete)

import Obsolete.projectMetadata
importlib.reload(Obsolete.projectMetadata)

from Obsolete.projectMetadata import ProjectObject


class ProjectQObject(ProjectObject, QObject):
	"""Handle Project file"""
	onWorkDirectoryUpdate = Signal()

	def __init__(self, ProjectFile=str()):
		QObject.__init__(self)
		ProjectObject.__init__(self, ProjectFile=ProjectFile)

	def set_WorkDirectory(self, work_directory=str):
		ProjectObject.set_WorkDirectory(self, work_directory=work_directory)
		self.onWorkDirectoryUpdate.emit()