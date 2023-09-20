# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

from gui.core.json_themes import Themes
from gui.widgets.py_push_button.py_push_button import PyPushButton
from gui.widgets.py_task_button.py_task_button import PyTaskButton

# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
border: none;
'''


class PyGroups(QWidget):
    TASK = 2
    MAXIMUM_HEIGHT = 45 * TASK
    IS_EXPANDED = True

    def __init__(
            self,
            parent=None
    ):
        super().__init__()

        # THEMES
        themes = Themes()
        self.themes = themes.items

        # SETUP UI
        self.setup_ui()

        # FUNCTION UI
        self.function_ui()

        # PARENT
        if parent != None:
            self.setParent(parent)

        self.setMaximumHeight(35 + PyGroups.MAXIMUM_HEIGHT)

    def setup_ui(self):
        # ADD LAYOUT
        self.lists_layout = QVBoxLayout(self)
        self.lists_layout.setContentsMargins(2, 2, 2, 2)
        self.lists_layout.setSpacing(2)

        # TASK VIEW WIDGET
        self.list_view_expandable = QWidget()
        # self.list_view_expandable.setMaximumHeight(45*PyGroups.TASK)
        self.list_view_expandable_layout = QVBoxLayout(self.list_view_expandable)
        self.list_view_expandable_layout.setContentsMargins(0, 0, 0, 0)

        # REMAINING BUTTON
        self.list_button = PyPushButton(
            text=" Remaining Tasks ",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.list_button.setMinimumHeight(30)
        self.list_button.setMaximumWidth(200)

        # CREATE TASK VIEW SCROLL AREA
        self.list_view_scroll_area = QScrollArea()
        self.list_view_scroll_area.setStyleSheet(style)
        self.widget = QWidget()
        # self.widget.setMaximumHeight(45*PyGroups.TASK)
        self.list_view_scroll_area_layout = QVBoxLayout()
        self.list_view_scroll_area_layout.setContentsMargins(0, 0, 0, 0)
        self.list_view_scroll_area_layout.setSpacing(2)
        self.widget.setLayout(self.list_view_scroll_area_layout)
        self.list_view_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.list_view_scroll_area.(QAbstractItemView.ScrollPerPixel)
        self.list_view_scroll_area.setWidgetResizable(True)
        self.list_view_scroll_area.setWidget(self.widget)

        # TASK BUTTON
        self.task_btn = PyTaskButton(
            parent=self.list_view_scroll_area
        )

        # ADD WIDGETS
        self.lists_layout.addWidget(self.list_button)
        self.list_view_expandable_layout.addWidget(self.list_view_scroll_area)
        self.lists_layout.addWidget(self.list_view_expandable)
        self.list_view_scroll_area_layout.addWidget(self.task_btn)
        self.list_view_scroll_area_layout.setAlignment(Qt.AlignTop)

    def function_ui(self):
        self.list_button.clicked.connect(self.expand_animation)

    def expand_animation(self):
        if PyGroups.IS_EXPANDED:
            # WIDGET HEIGHT
            # PyGroups.MAXIMUM_HEIGHT = self.widget.height()
            self.widget.setMaximumHeight(0)
            self.setMaximumHeight(70)
            PyGroups.IS_EXPANDED = False
        else:
            self.widget.setMaximumHeight(PyGroups.MAXIMUM_HEIGHT)
            self.setMaximumHeight(PyGroups.MAXIMUM_HEIGHT + 40)
            PyGroups.IS_EXPANDED = True
