# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT DB CORE
# ///////////////////////////////////////////////////////////////
from db_core import *

import uuid
from gui.core.json_themes import Themes
from gui.core.database import Database
from gui.uis.windows.main_window.functions_main_window import Functions
from gui.widgets.py_push_button.py_push_button import PyPushButton
from gui.widgets.py_line_edit.py_line_edit import PyLineEdit
from gui.widgets.py_combo_box.py_combo_box import PyComboBox
from gui.widgets.py_check_combo_box.py_check_combo_box import PyCheckComboBox


class PyCreateList(QWidget):
    LIST_STAT = False
    MAXIMUM_HEIGHT = 115
    MINIMUM_HEIGHT = 2

    def __init__(
            self,
            parent=None
    ):
        super().__init__()

        # THEME
        themes = Themes()
        self.themes = themes.items

        # SET UI
        self.setup_ui()

        # FUNCTION UI
        self.function_ui()

        # PARENT
        if parent != None:
            self.setParent(parent)

    def setup_ui(self):

        # ADD LAYOUT
        self.create_list_layout = QVBoxLayout(self)
        self.create_list_layout.setContentsMargins(2, 2, 2, 2)
        self.create_list_layout.setSpacing(2)

        # CREATE LIST WIDGET
        self.list_expandable_frame = QWidget()
        self.list_expandable_frame_layout = QVBoxLayout(self.list_expandable_frame)

        # CREATE LIST BUTTON
        self.create_list_btn = PyPushButton(
            text=" Create List ",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("icon_create.svg"))
        self.create_list_btn.setMinimumHeight(30)
        self.create_list_btn.setIcon(self.icon)

        # LIST NAME EDIT
        self.list_name_edit = PyLineEdit(
            text="",
            place_holder_text="List Name",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.list_name_edit.setMinimumHeight(30)

        # ADD TASK TO LIST FRAME
        self.add_task_to_list_frame = QFrame()
        self.add_task_to_list_frame.setMinimumHeight(30)
        self.add_task_to_list_layout = QHBoxLayout(self.add_task_to_list_frame)
        self.add_task_to_list_layout.setContentsMargins(0, 0, 0, 0)
        self.add_task_to_list_label = QLabel()
        self.add_task_to_list_label.setText("Add Tasks to List:")
        self.add_task_to_list_label.setMinimumHeight(30)
        self.add_task_to_list_layout.addWidget(self.add_task_to_list_label)
        self.add_task_combo = PyCheckComboBox(
            parent=self.add_task_to_list_frame,
            data=TASK_NAMES
        )
        self.add_task_to_list_layout.addWidget(self.add_task_combo)

        # LIST SAVE BUTTON
        self.list_save_btn = PyPushButton(
            text="Save",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.list_save_btn.setMinimumHeight(30)

        # ADD WIDGETS
        self.create_list_layout.addWidget(self.create_list_btn)
        self.list_expandable_frame_layout.addWidget(self.list_name_edit)
        self.list_expandable_frame_layout.addWidget(self.add_task_to_list_frame)
        self.list_expandable_frame_layout.addWidget(self.list_save_btn)
        self.create_list_layout.addWidget(self.list_expandable_frame)

        self.list_expandable_frame.setMinimumHeight(PyCreateList.MINIMUM_HEIGHT)
        self.list_expandable_frame.setMaximumHeight(PyCreateList.MINIMUM_HEIGHT)

    def function_ui(self):
        self.create_list_btn.clicked.connect(self.list_expandable_animation)
        self.list_save_btn.clicked.connect(self.save_list)

    def list_expandable_animation(self):
        self.list_animation = QPropertyAnimation(self.list_expandable_frame, b"maximumHeight")
        self.list_animation.stop()
        if self.list_expandable_frame.height() == PyCreateList.MAXIMUM_HEIGHT:
            self.list_animation.setStartValue(self.list_expandable_frame.height())
            self.list_animation.setEndValue(PyCreateList.MINIMUM_HEIGHT)
            PyCreateList.LIST_STAT = False
        else:
            self.list_animation.setStartValue(self.list_expandable_frame.height())
            self.list_animation.setEndValue(PyCreateList.MAXIMUM_HEIGHT)
            PyCreateList.LIST_STAT = True
        self.list_animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.list_animation.setDuration(500)
        self.list_animation.start()

    def save_list(self):
        Database.add_list(
            self=Database(),
            list_id=str(uuid.uuid4())[:5],
            list_name=self.list_name_edit.text()
        )
        Database.get_list_details(Database())
        self.all_clear()

    def all_clear(self):
        self.list_name_edit.clear()
        for idx in range(self.add_task_combo.count()):
            self.add_task_combo.setItemChecked(idx, False)
        self.add_task_combo.setCurrentIndex(0)
