# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *


class PyTimeEdit(QTimeEdit):
    def __init__(
            self,
            parent=None
    ):
        super().__init__(parent)

        # PARENT
        if parent != None:
            self.setParent(parent)
