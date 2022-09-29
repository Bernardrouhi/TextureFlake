import importlib
import substance_painter.ui

from .widgets import textureFlakeMainWindow
importlib.reload(textureFlakeMainWindow)

from .widgets.textureFlakeMainWindow import TextureFlakeMainWindow

TF_APP = []

def launchTextureFlake():
    widget = TextureFlakeMainWindow(substance_painter.ui.get_main_window())
    # Add to the interface
    substance_painter.ui.add_dock_widget(widget, 1)
    # Store widget
    TF_APP.append(widget)

def closeTextureFlake():
    # remove the widget
    if TF_APP:
        substance_painter.ui.delete_ui_element(TF_APP[0])
    TF_APP.clear()
