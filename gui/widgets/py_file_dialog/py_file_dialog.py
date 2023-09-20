# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QPushButton {{
	border: none;
    padding-left: 10px;
    padding-right: 5px;
    color: {_color};
	border-radius: {_radius};	
	background-color: {_bg_color};
}}
QPushButton:hover {{
	background-color: {_bg_color_hover};
}}
QPushButton:pressed {{	
	background-color: {_bg_color_pressed};
}}
'''


class PyFileDialog(QPushButton):
    def __init__(
            self,
            text,
            radius,
            color,
            bg_color,
            bg_color_hover,
            bg_color_pressed,
            parent=None,
    ):
        super().__init__()

        # SET PARAMETRES
        self.setText(text)
        if parent != None:
            self.setParent(parent)
        self.setCursor(Qt.PointingHandCursor)

        # SET STYLESHEET
        custom_style = style.format(
            _color=color,
            _radius=radius,
            _bg_color=bg_color,
            _bg_color_hover=bg_color_hover,
            _bg_color_pressed=bg_color_pressed
        )
        self.setStyleSheet(custom_style)

        self.clicked.connect(self.getfile)

    def getfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "Exec files (*.exe)")
        print(fname)


# def main():
#     app = QApplication(sys.argv)
#     ex = PyFileDialog(
#         text=" Delete ",
#         radius=8,
#         color="",
#         bg_color="",
#         bg_color_hover="",
#         bg_color_pressed=""
#     )
#     ex.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()
