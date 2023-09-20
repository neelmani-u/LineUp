# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# PY COMBO BOX
# ///////////////////////////////////////////////////////////////
from gui.widgets.py_combo_box.py_combo_box import PyComboBox

# IMPORT MODULES AND PACKAGES
# ///////////////////////////////////////////////////////////////
import sys


class PyCheckComboBox(PyComboBox):
    def __init__(self, parent=None, data=None):
        super(PyCheckComboBox, self).__init__(parent, data)
        self.view().pressed.connect(self.handleItemPressed)
        self._changed = False

    def handleItemPressed(self, index):
        item = self.model().itemFromIndex(index)
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
        else:
            item.setCheckState(Qt.Checked)
        self._changed = True

    def hidePopup(self):
        if not self._changed:
            super(PyCheckComboBox, self).hidePopup()
        self._changed = False

    def itemChecked(self, index):
        item = self.model().item(index, self.modelColumn())
        # print(item.checkState() == QtCore.Qt.Checked)
        return item.checkState() == Qt.Checked

    def setItemChecked(self, index, checked=True):
        item = self.model().item(index, self.modelColumn())
        if checked:
            item.setCheckState(Qt.Checked)
        else:
            item.setCheckState(Qt.Unchecked)

        self.itemChecked(index)


# class Window(QWidget):
#     def __init__(self):
#         super(Window, self).__init__()
#         self.combo = PyCheckComboBox(self)
#         self.submit = QPushButton(self)
#         self.submit.setObjectName(u"submitBtn")
#         # for index in range(6):
#         #     self.combo.addItem('Item %d' % index)
#         #     self.combo.setItemChecked(index, False)
#         for index, item in enumerate(data):
#             self.combo.addItem(data[item], item)
#             self.combo.setItemChecked(index, False)
#         layout = QVBoxLayout(self)
#         layout.addWidget(self.combo)
#         layout.addWidget(self.submit)
#
#         self.ifClicked()
#
#     def ifClicked(self):
#         self.submit.clicked.connect(lambda: self.check())
#
#     def check(self):
#         for i in range(6):
#             print(self.combo.itemChecked(i))
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#     window.setGeometry(500, 300, 200, 100)
#     window.show()
#     sys.exit(app.exec_())
