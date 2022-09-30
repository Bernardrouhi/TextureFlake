import importlib

from .widgets import textureFlakeMainWindow
importlib.reload(textureFlakeMainWindow)
from .core import substanceHelper as SP
importlib.reload(SP)


from .widgets.textureFlakeMainWindow import TextureFlakeMainWindow

TF_APP = []

def launchTextureFlake():
    widget = TextureFlakeMainWindow(SP.get_SubstanceQMainWindow())
    # Add to the interface
    SP.add_MainWindow(widget)
    # Store widget
    TF_APP.append(widget)

def closeTextureFlake():
    # remove the widget
    if TF_APP:
        SP.remove_MainWindow(TF_APP[0])
    TF_APP.clear()
