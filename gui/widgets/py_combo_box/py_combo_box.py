# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QComboBox {{
    border: {_border};
    border-radius: {_radius}px;
    background-color: {_bg_color};
    color: {_color};

    padding: 1px 1px 1px 3px;
}}

QComboBox::drop-down {{
    border: {_border};
}}

QComboBox::down-arrow {{
    
    width: 14px;
    height: 14px;
}}
'''


# PY COMBO BOX
# ///////////////////////////////////////////////////////////////
class PyComboBox(QComboBox):

    def __init__(
            self,
            parent,
            data,
            radius=8,
            border="none",
            bg_color="#3c4454",
            color="#FFF",
            text_size=14,
            height=35
    ):
        super().__init__()

        if parent is not None:
            self.setParent(parent)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        # SET STYLESHEET
        custom_style = style.format(
            _border=border,
            _radius=radius,
            _bg_color=bg_color,
            _color=color,
            _text_size=text_size
        )
        self.setStyleSheet(custom_style)

        # OPTIONS IN COMBOBOX
        self.addItems(data)

