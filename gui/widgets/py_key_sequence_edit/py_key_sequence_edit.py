# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *


class PyKeySequenceEdit(QKeySequenceEdit):
    def keyPressEvent(self, event):
        super().keyPressEvent(event)

        sequenceString = self.keySequence().toString(QKeySequence.NativeText)
        if sequenceString:
            last_key_stroke = sequenceString.split(',')[-1].strip()
            self.setKeySequence(QKeySequence(last_key_stroke))