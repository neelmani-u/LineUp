# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT STYLE
# ///////////////////////////////////////////////////////////////
from .style import *


# PY TAB WIDGET
# ///////////////////////////////////////////////////////////////
class PyTabWidget(QTabWidget):
    def __init__(
            self,
            radius=5,
            bg_color="#444",
            selection_color="#FFF",
            parent=None,
    ):
        super().__init__()

        # PARAMETERS
        if parent != None:
            self.setParent(parent)

        # SET STYLESHEET
        self.set_stylesheet(
            radius,
            bg_color,
            selection_color
        )

    def set_stylesheet(
            self,
            radius,
            bg_color,
            selection_color
    ):
        # APPLY STYLESHEET
        style_format = style.format(
            _radius=radius,
            _bg_color=bg_color,
            _selection_color=selection_color
        )
        self.setStyleSheet(style_format)
