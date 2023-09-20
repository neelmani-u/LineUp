# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT DB CORE
# ///////////////////////////////////////////////////////////////
from db_core import *

from gui.core.json_themes import Themes
from gui.core.functions import Functions
from gui.widgets.py_push_button.py_push_button import PyPushButton
from gui.widgets.py_task_button.py_task_button import PyTaskButton

# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
border: none;
'''


class PyTaskCompleted(QWidget):
    TASK_COMPLETED = len(COMPLETED_TASK_DATA)
    if TASK_COMPLETED == 0: TASK_COMPLETED = 1
    MAXIMUM_HEIGHT = 45 * TASK_COMPLETED
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

        self.setStyleSheet("border: 1px solid white;")

        # PARENT
        if parent != None:
            self.setParent(parent)

        # self.setMaximumHeight(35 + PyTaskCompleted.MAXIMUM_HEIGHT)

    def setup_ui(self):
        # ADD LAYOUT
        self.myday_task_completed_layout = QVBoxLayout(self)
        self.myday_task_completed_layout.setContentsMargins(2, 2, 2, 2)
        self.myday_task_completed_layout.setSpacing(2)
        # self.setLayout(self.myday_task_completed_layout)

        # TASK VIEW WIDGET
        self.task_view_expandable = QWidget()
        self.task_view_expandable.setMaximumHeight(45*PyTaskCompleted.TASK_COMPLETED)
        self.task_view_expandable_layout = QVBoxLayout(self.task_view_expandable)
        self.task_view_expandable_layout.setContentsMargins(0, 0, 0, 0)
        # self.task_view_expandable.setLayout(self.task_view_expandable_layout)

        # REMAINING BUTTON
        self.completed_button = PyPushButton(
            text=" Completed Tasks ",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.completed_button.setMinimumHeight(30)
        self.completed_button.setMaximumWidth(200)

        # CREATE TASK VIEW SCROLL AREA
        self.myday_task_view_scroll_area = QScrollArea()
        self.myday_task_view_scroll_area.setStyleSheet(style)
        self.widget = QWidget()
        self.widget.setMaximumHeight(45 * PyTaskCompleted.TASK_COMPLETED)
        self.myday_task_view_scroll_area_layout = QVBoxLayout()
        self.myday_task_view_scroll_area_layout.setContentsMargins(0, 0, 0, 0)
        self.myday_task_view_scroll_area_layout.setSpacing(2)
        self.widget.setLayout(self.myday_task_view_scroll_area_layout)
        self.myday_task_view_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.myday_task_view_scroll_area.(QAbstractItemView.ScrollPerPixel)
        self.myday_task_view_scroll_area.setWidgetResizable(True)
        self.myday_task_view_scroll_area.setWidget(self.widget)

        # TASK BUTTON
        # print(COMPLETED_TASK_DATA)
        self.setup_task_buttons(COMPLETED_TASK_DATA)
        # self.myday_task_completed_layout.addWidget(self.task_view_expandable)

        # ADD WIDGETS
        self.myday_task_completed_layout.addWidget(self.completed_button)
        self.task_view_expandable_layout.addWidget(self.myday_task_view_scroll_area)
        self.myday_task_completed_layout.addWidget(self.task_view_expandable, 0, Qt.AlignTop)
        self.myday_task_view_scroll_area_layout.setAlignment(Qt.AlignTop)

    def function_ui(self):
        self.completed_button.clicked.connect(self.expand_animation)

    def setup_task_buttons(self, completed_task_data):
        for row in completed_task_data:
            self.task_btn = PyTaskButton(
                task_id=row[0],
                task_name=row[1],
                parent=self.myday_task_view_scroll_area
            )
            # self.setMaximumHeight(self.height() + 45)
            self.myday_task_view_scroll_area_layout.addWidget(self.task_btn)
            self.task_btn.tick_btn.set_icon(Functions.set_svg_icon("icon_task_tick.svg"))
            if row[10] == 1:
                self.task_btn.task_star_btn.set_icon(Functions.set_svg_icon("icon_star.svg"))

    def expand_animation(self):
        if PyTaskCompleted.IS_EXPANDED:
            # WIDGET HEIGHT
            PyTaskCompleted.MAXIMUM_HEIGHT = self.widget.height()
            self.widget.setMaximumHeight(0)
            # self.setMaximumHeight(70)
            PyTaskCompleted.IS_EXPANDED = False
        else:
            self.widget.setMaximumHeight(PyTaskCompleted.MAXIMUM_HEIGHT)
            # self.setMaximumHeight(PyTaskCompleted.MAXIMUM_HEIGHT + 40)
            # self.task_view_expandable.setMaximumHeight(PyTaskCompleted.MAXIMUM_HEIGHT)
            PyTaskCompleted.IS_EXPANDED = True
