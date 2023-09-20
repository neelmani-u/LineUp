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


class PyTaskRemaining(QWidget):
    TASK_REMAINING = len(REMAINING_TASK_DATA)
    if TASK_REMAINING == 0: TASK_REMAINING = 1
    MAXIMUM_HEIGHT = 45 * TASK_REMAINING
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

        # self.setMaximumHeight(35 + PyTaskRemaining.MAXIMUM_HEIGHT)

    def setup_ui(self):
        # ADD LAYOUT
        self.myday_task_remaining_layout = QVBoxLayout(self)
        self.myday_task_remaining_layout.setContentsMargins(2, 2, 2, 2)
        self.myday_task_remaining_layout.setSpacing(2)

        # TASK VIEW WIDGET
        self.task_view_expandable = QWidget()
        self.task_view_expandable.setMaximumHeight(45*PyTaskRemaining.TASK_REMAINING)
        self.task_view_expandable_layout = QVBoxLayout(self.task_view_expandable)
        self.task_view_expandable_layout.setContentsMargins(0, 0, 0, 0)

        # REMAINING BUTTON
        self.remaining_button = PyPushButton(
            text=" Remaining Tasks ",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.remaining_button.setMinimumHeight(30)
        self.remaining_button.setMaximumWidth(200)

        # CREATE TASK VIEW SCROLL AREA
        self.myday_task_view_scroll_area = QScrollArea()
        self.myday_task_view_scroll_area.setStyleSheet(style)
        self.widget = QWidget()
        self.widget.setMaximumHeight(45*PyTaskRemaining.TASK_REMAINING)
        self.myday_task_view_scroll_area_layout = QVBoxLayout()
        self.myday_task_view_scroll_area_layout.setContentsMargins(0, 0, 0, 0)
        self.myday_task_view_scroll_area_layout.setSpacing(2)
        self.widget.setLayout(self.myday_task_view_scroll_area_layout)
        self.myday_task_view_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.myday_task_view_scroll_area.(QAbstractItemView.ScrollPerPixel)
        self.myday_task_view_scroll_area.setWidgetResizable(True)
        self.myday_task_view_scroll_area.setWidget(self.widget)

        # TASK BUTTON
        # print(REMAINING_TASK_DATA)
        # rem_task_data = Database.get_task_details(Database())
        self.setup_task_buttons(REMAINING_TASK_DATA)

        # ADD WIDGETS
        self.myday_task_remaining_layout.addWidget(self.remaining_button)
        self.task_view_expandable_layout.addWidget(self.myday_task_view_scroll_area)
        self.myday_task_remaining_layout.addWidget(self.task_view_expandable)
        self.myday_task_view_scroll_area_layout.setAlignment(Qt.AlignTop)

    def function_ui(self):
        self.remaining_button.clicked.connect(self.expand_animation)

    def setup_task_buttons(self, remaining_task_data):
        for row in remaining_task_data:
            self.task_btn = PyTaskButton(
                task_id=row[0],
                task_name=row[1],
                parent=self.myday_task_view_scroll_area
            )
            self.myday_task_view_scroll_area_layout.addWidget(self.task_btn)
            if row[10] == 1:
                self.task_btn.task_star_btn.set_icon(Functions.set_svg_icon("icon_star.svg"))
        # print(self.task_btn)

    def expand_animation(self):
        if PyTaskRemaining.IS_EXPANDED:
            # WIDGET HEIGHT
            PyTaskRemaining.MAXIMUM_HEIGHT = self.widget.height()
            self.widget.setMaximumHeight(0)
            # self.setMaximumHeight(70)
            PyTaskRemaining.IS_EXPANDED = False
        else:
            self.widget.setMaximumHeight(PyTaskRemaining.MAXIMUM_HEIGHT)
            # self.setMaximumHeight(PyTaskRemaining.MAXIMUM_HEIGHT + 40)
            PyTaskRemaining.IS_EXPANDED = True
