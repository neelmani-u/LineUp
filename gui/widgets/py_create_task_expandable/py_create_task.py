# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT DB CORE
# ///////////////////////////////////////////////////////////////
from db_core import *

import uuid
import datetime
import calendar
from datetime import date
from gui.core.json_themes import Themes
from gui.uis.windows.main_window.functions_main_window import Functions
from gui.widgets.py_push_button.py_push_button import PyPushButton
from gui.widgets.py_line_edit.py_line_edit import PyLineEdit
from gui.widgets.py_combo_box.py_combo_box import PyComboBox
from gui.widgets.py_check_combo_box.py_check_combo_box import PyCheckComboBox
from gui.widgets.py_time_edit.py_time_edit import PyTimeEdit


class PyCreateTask(QWidget):
    TASK_STAT = False
    MAXIMUM_HEIGHT = 260
    MINIMUM_HEIGHT = 2

    def __init__(
            self,
            parent=None
    ):
        super().__init__()

        # THEME
        themes = Themes()
        self.themes = themes.items

        # SETUP UI
        self.setup_ui()

        # FUNCTION UI
        self.function_ui()

        # PARENT
        if parent != None:
            self.setParent(parent)

    def setup_ui(self):
        # CREATE TASK FRAME
        # self.create_task_frame = QFrame()

        # ADD LAYOUT
        self.create_task_layout = QVBoxLayout(self)
        # self.create_task_layout = QVBoxLayout(self.create_task_frame)
        self.create_task_layout.setContentsMargins(2, 2, 2, 2)
        self.create_task_layout.setSpacing(2)

        self.task_expandable_frame = QWidget()
        self.task_expandable_frame_layout = QVBoxLayout(self.task_expandable_frame)

        # CREATE TASK BUTTON
        self.create_btn = PyPushButton(
            text=" Create Task ",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("icon_create.svg"))
        self.create_btn.setMinimumHeight(30)
        self.create_btn.setIcon(self.icon)

        # TASK NAME EDIT
        self.task_name_edit = PyLineEdit(
            text="",
            place_holder_text="Task Name",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.task_name_edit.setMinimumHeight(30)

        # DUE DATE FRAME
        self.due_date_frame = QFrame()
        self.due_date_frame.setMinimumHeight(30)
        self.due_date_layout = QHBoxLayout(self.due_date_frame)
        self.due_date_layout.setContentsMargins(0, 0, 0, 0)
        # self.due_date_layout.setSpacing(2)
        self.due_date_label = QLabel()
        self.due_date_label.setText("Add Due Date:")
        self.due_date_label.setMinimumHeight(30)
        # self.due_date_label.setAlignment(Qt.AlignLeft)
        self.due_date_layout.addWidget(self.due_date_label)
        self.due_date_combo = PyComboBox(
            parent=self.due_date_frame,
            data=[
                "Today",
                "Tomorrow",
                "Next Week",
                # "Pick a Date"
            ]
        )
        self.due_date_layout.addWidget(self.due_date_combo)

        # REMIND ME FRAME
        self.remind_me_frame = QFrame()
        self.remind_me_frame.setMinimumHeight(30)
        self.remind_me_layout = QHBoxLayout(self.remind_me_frame)
        self.remind_me_layout.setContentsMargins(0, 0, 0, 0)
        self.remind_me_label = QLabel()
        self.remind_me_label.setText("Remind me:")
        self.remind_me_label.setMinimumHeight(30)
        # self.remind_me_label.setAlignment(Qt.AlignLeft)
        self.remind_me_layout.addWidget(self.remind_me_label)
        self.remind_date_combo = PyComboBox(
            parent=self.remind_me_frame,
            data=[
                "Later Today",
                "Tomorrow",
                "Next Week",
                # "Pick a Date & Time"
            ]
        )
        self.remind_me_time = PyTimeEdit(
            parent=self.remind_me_frame
        )
        self.remind_me_time.setMinimumHeight(30)
        self.remind_me_layout.addWidget(self.remind_date_combo)
        self.remind_me_layout.addWidget(self.remind_me_time)

        # REPEAT FRAME
        self.repeat_task_frame = QFrame()
        self.repeat_task_frame.setMinimumHeight(30)
        self.repeat_task_layout = QHBoxLayout(self.repeat_task_frame)
        self.repeat_task_layout.setContentsMargins(0, 0, 0, 0)
        self.repeat_task_label = QLabel()
        self.repeat_task_label.setText("Repeat:")
        self.repeat_task_label.setMinimumHeight(30)
        # self.repeat_task_label.setAlignment(Qt.AlignLeft)
        self.repeat_task_layout.addWidget(self.repeat_task_label)
        self.repeat_task_combo = PyComboBox(
            parent=self.repeat_task_frame,
            data=[
                "Daily",
                "Weekdays",
                "Monthly",
                "Yearly",
                # "Custom"
            ]
        )
        self.repeat_task_layout.addWidget(self.repeat_task_combo)

        # PRIORITY LEVEL
        self.task_priority_frame = QFrame()
        self.task_priority_frame.setMinimumHeight(30)
        self.task_priority_layout = QHBoxLayout(self.task_priority_frame)
        self.task_priority_layout.setContentsMargins(0, 0, 0, 0)
        self.task_priority_label = QLabel("Priority Level:")
        self.task_priority_label.setMinimumHeight(30)
        self.task_priority_layout.addWidget(self.task_priority_label)
        self.task_priority_combo = PyComboBox(
            parent=self.task_priority_frame,
            data=[
                "LOW",
                "MEDIUM",
                "HIGH"
            ]
        )
        self.task_priority_layout.addWidget(self.task_priority_combo)

        # ADD TO LIST FRAME
        self.add_to_list_frame = QFrame()
        self.add_to_list_frame.setMinimumHeight(30)
        self.add_to_list_layout = QHBoxLayout(self.add_to_list_frame)
        self.add_to_list_layout.setContentsMargins(0, 0, 0, 0)
        self.add_to_list_label = QLabel()
        self.add_to_list_label.setText("Add to List")
        self.add_to_list_label.setMinimumHeight(30)
        # self.add_to_list_label.setAlignment(Qt.AlignLeft)
        self.add_to_list_layout.addWidget(self.add_to_list_label)
        self.add_to_list_combo = PyComboBox(
            parent=self.add_to_list_frame,
            data=VAL_LIST
        )
        self.add_to_list_layout.addWidget(self.add_to_list_combo)

        # MARK IMPORTANT & SAVE BUTTON
        self.mark_imp_and_save_frame = QFrame()
        self.mark_imp_and_save_frame.setMinimumHeight(30)
        self.mark_imp_and_save_layout = QHBoxLayout(self.mark_imp_and_save_frame)
        self.mark_imp_and_save_layout.setContentsMargins(0, 0, 0, 0)
        self.mark_imp_check_box = QCheckBox()
        self.mark_imp_check_box.setText("Mark Important")
        self.mark_imp_check_box.setMinimumHeight(30)
        self.mark_imp_and_save_layout.addWidget(self.mark_imp_check_box)
        self.task_save_btn = PyPushButton(
            text="Save",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.task_save_btn.setMinimumHeight(30)
        self.mark_imp_and_save_layout.addWidget(self.task_save_btn)

        # ADD WIDGETS
        self.create_task_layout.addWidget(self.create_btn)
        self.task_expandable_frame_layout.addWidget(self.task_name_edit)
        self.task_expandable_frame_layout.addWidget(self.due_date_frame)
        self.task_expandable_frame_layout.addWidget(self.remind_me_frame)
        self.task_expandable_frame_layout.addWidget(self.repeat_task_frame)
        self.task_expandable_frame_layout.addWidget(self.task_priority_frame)
        self.task_expandable_frame_layout.addWidget(self.add_to_list_frame)
        self.task_expandable_frame_layout.addWidget(self.mark_imp_and_save_frame)
        self.create_task_layout.addWidget(self.task_expandable_frame)

        self.task_expandable_frame.setMinimumHeight(PyCreateTask.MINIMUM_HEIGHT)
        self.task_expandable_frame.setMaximumHeight(PyCreateTask.MINIMUM_HEIGHT)

    def function_ui(self):
        self.create_btn.clicked.connect(self.task_expandable_animation)
        self.task_save_btn.clicked.connect(self.save_task)

    def task_expandable_animation(self):
        self.task_animation = QPropertyAnimation(self.task_expandable_frame, b"maximumHeight")
        self.task_animation.stop()
        if self.task_expandable_frame.height() == PyCreateTask.MAXIMUM_HEIGHT:
            self.task_animation.setStartValue(self.task_expandable_frame.height())
            self.task_animation.setEndValue(PyCreateTask.MINIMUM_HEIGHT)
            PyCreateTask.TASK_STAT = False
        else:
            self.task_animation.setStartValue(self.task_expandable_frame.height())
            self.task_animation.setEndValue(PyCreateTask.MAXIMUM_HEIGHT)
            PyCreateTask.TASK_STAT = True
        self.task_animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.task_animation.setDuration(500)
        self.task_animation.start()

    def save_task(self):
        list_pos = VAL_LIST.index(self.add_to_list_combo.currentText())
        Database.add_task(
            self=Database(),
            task_id=str(uuid.uuid4())[:5],
            task_name=self.task_name_edit.text(),
            created_date=date.today().strftime("%d/%m/%y"),
            due_date=self.date_decode(self.due_date_combo),
            remind_date=self.date_decode(self.remind_date_combo),
            remind_time=self.remind_me_time.time().toString("hh:mm"),
            repeat=self.repeat_decode(),
            my_day=self.check_for_myday(),
            priority_lvl=self.task_priority_combo.currentText(),
            status=False,
            important=self.mark_imp_check_box.isChecked(),
            list_id=KEY_LIST[list_pos]
        )
        print(Database.get_task_details(Database()))
        self.all_clear()

    def date_decode(self, combo_box):
        today = date.today()
        idx = combo_box.currentIndex()
        if idx == 0:
            return today.strftime("%d/%m/%y")
        elif idx == 1:
            return (today + datetime.timedelta(days=1)).strftime("%d/%m/%y")
        elif idx == 2:
            return (today + datetime.timedelta(days=7)).strftime("%d/%m/%y")

    def repeat_decode(self):
        today = date.today()
        idx = self.repeat_task_combo.currentIndex()
        if idx == 0:
            return today.strftime("%d/%m/%y")
        elif idx == 1:
            return (today + datetime.timedelta(days=7)).strftime("%d/%m/%y")
        elif idx == 2:
            days_in_month = calendar.monthrange(today.year, today.month)[1]
            return (today + datetime.timedelta(days=days_in_month)).strftime("%d/%m/%y")
        elif idx == 3:
            repeat_date = today.replace(today.year + 1)
            return repeat_date.strftime("%d/%m/%y")

    def check_for_myday(self):
        idx = self.due_date_combo.currentIndex()
        if idx == 0:
            return True
        else:
            return False

    def all_clear(self):
        self.task_name_edit.clear()
        self.due_date_combo.setCurrentIndex(0)
        self.remind_date_combo.setCurrentIndex(0)
        self.remind_me_time.setTime(QTime(0, 0, 0, 0))
        self.repeat_task_combo.setCurrentIndex(0)
        self.add_to_list_combo.setCurrentIndex(0)
        self.task_priority_combo.setCurrentIndex(0)
        self.mark_imp_check_box.setCheckState(Qt.Unchecked)
