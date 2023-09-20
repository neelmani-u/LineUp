# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

from gui.core.json_themes import Themes
from gui.uis.windows.main_window.functions_main_window import Functions
from gui.widgets.py_push_button.py_push_button import PyPushButton
from gui.widgets.py_line_edit.py_line_edit import PyLineEdit
from gui.widgets.py_combo_box.py_combo_box import PyComboBox
from gui.widgets.py_check_combo_box.py_check_combo_box import PyCheckComboBox


class PyCreateGroup(QWidget):
    GROUP_STAT = False
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
        self.create_group_layout = QVBoxLayout(self)
        self.create_group_layout.setContentsMargins(2, 2, 2, 2)
        self.create_group_layout.setSpacing(2)

        # CREATE LIST WIDGET
        self.group_expandable_frame = QWidget()
        self.group_expandable_frame_layout = QVBoxLayout(self.group_expandable_frame)

        # CREATE LIST BUTTON
        self.create_group_btn = PyPushButton(
            text=" Create Group ",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("icon_create.svg"))
        self.create_group_btn.setMinimumHeight(30)
        self.create_group_btn.setIcon(self.icon)

        # LIST NAME EDIT
        self.group_name_edit = PyLineEdit(
            text="",
            place_holder_text="Group Name",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.group_name_edit.setMinimumHeight(30)

        # ADD TASK TO LIST FRAME
        self.add_list_to_group_frame = QFrame()
        self.add_list_to_group_frame.setMinimumHeight(30)
        self.add_list_to_group_layout = QHBoxLayout(self.add_list_to_group_frame)
        self.add_list_to_group_layout.setContentsMargins(0, 0, 0, 0)
        self.add_list_to_group_label = QLabel()
        self.add_list_to_group_label.setText("Add Lists to Group:")
        self.add_list_to_group_label.setMinimumHeight(30)
        self.add_list_to_group_layout.addWidget(self.add_list_to_group_label)
        self.add_group_combo = PyCheckComboBox(
            parent=self.add_list_to_group_frame,
            data=[
                "G1",
                "G2"
            ]
        )
        self.add_list_to_group_layout.addWidget(self.add_group_combo)

        # LIST SAVE BUTTON
        self.group_save_btn = PyPushButton(
            text="Save",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.group_save_btn.setMinimumHeight(30)

        # ADD WIDGETS
        self.create_group_layout.addWidget(self.create_group_btn)
        self.group_expandable_frame_layout.addWidget(self.group_name_edit)
        self.group_expandable_frame_layout.addWidget(self.add_list_to_group_frame)
        self.group_expandable_frame_layout.addWidget(self.group_save_btn)
        self.create_group_layout.addWidget(self.group_expandable_frame)

        self.group_expandable_frame.setMinimumHeight(PyCreateGroup.MINIMUM_HEIGHT)
        self.group_expandable_frame.setMaximumHeight(PyCreateGroup.MINIMUM_HEIGHT)

    def function_ui(self):
        self.create_group_btn.clicked.connect(self.group_expandable_animation)

    def group_expandable_animation(self):
        self.group_animation = QPropertyAnimation(self.group_expandable_frame, b"maximumHeight")
        self.group_animation.stop()
        if self.group_expandable_frame.height() == PyCreateGroup.MAXIMUM_HEIGHT:
            self.group_animation.setStartValue(self.group_expandable_frame.height())
            self.group_animation.setEndValue(PyCreateGroup.MINIMUM_HEIGHT)
            PyCreateGroup.GROUP_STAT = False
        else:
            self.group_animation.setStartValue(self.group_expandable_frame.height())
            self.group_animation.setEndValue(PyCreateGroup.MAXIMUM_HEIGHT)
            PyCreateGroup.GROUP_STAT = True
        self.group_animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.group_animation.setDuration(500)
        self.group_animation.start()
