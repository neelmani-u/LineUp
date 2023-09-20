# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT DB CORE
# ///////////////////////////////////////////////////////////////
from db_core import *

import importlib
from gui.core.database import Database
from gui.core.json_settings import Settings
from gui.core.json_themes import Themes
from gui.widgets.py_push_button.py_push_button import PyPushButton
# from gui.widgets.py_task_button.py_task_button import PyTaskButton
from gui.widgets.py_combo_box.py_combo_box import PyComboBox
from gui.widgets.py_time_edit.py_time_edit import PyTimeEdit
from gui.widgets.py_toggle.py_toggle import PyToggle
from gui.widgets.py_line_edit.py_line_edit import PyLineEdit


class PyTaskEditDialog(QDialog):

    def __init__(self, task_name):
        super().__init__()

        # SETTINGS
        settings = Settings()
        self.settings = settings.items

        # THEMES
        themes = Themes()
        self.themes = themes.items

        self.setWindowTitle("Edit Task")
        self.setStyleSheet(f'''
            font: {self.settings["font"]["text_size"]}pt "{self.settings["font"]["family"]}";
            color: {self.themes["app_color"]["text_foreground"]};
            background-color: {self.themes["app_color"]["dark_four"]};
        ''')
        self.setMinimumHeight(300)
        self.setMaximumHeight(400)

        # SETUP UI
        self.setup_ui()

        # FUNCTION UI
        self.function_ui()

        # EXTRACT DATA
        self.extract(task_name)

    def setup_ui(self):
        # TASK NAME EDIT
        self.task_name_edit = PyLineEdit(
            text="Edit Task Name",
            place_holder_text="Task Name",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.task_name_edit.setMinimumHeight(35)

        self.save_n_delete_frame = QFrame()
        self.save_n_delete_layout = QHBoxLayout(self.save_n_delete_frame)
        self.save_n_delete_layout.setContentsMargins(0, 0, 0, 0)
        self.save_btn = PyPushButton(
            text=" Save ",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.save_btn.setMaximumHeight(35)

        self.delete_btn = PyPushButton(
            text=" Delete ",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.delete_btn.setMinimumHeight(35)

        self.save_n_delete_layout.addWidget(self.save_btn)
        self.save_n_delete_layout.addWidget(self.delete_btn)

        # self.dialog_btn = QDialogButtonBox.Save | QDialogButtonBox.Cancel

        # self.task_edit_box = QDialogButtonBox(self.dialog_btn)
        # self.task_edit_box.accepted.connect(self.accept)
        # self.task_edit_box.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        # task_btn = PyTaskButton(
        #     parent=self.layout
        # )
        self.add_to_myday_frame = QFrame()
        self.add_to_myday_frame.setMinimumHeight(30)
        self.add_to_myday_layout = QHBoxLayout(self.add_to_myday_frame)
        self.add_to_myday_layout.setContentsMargins(0, 0, 0, 0)
        self.myday = QLabel()
        self.myday.setText("Add To My Day:")
        self.myday.setMinimumHeight(30)
        self.add_to_myday_layout.addWidget(self.myday)
        self.add_to_myday = PyToggle(
            width=55,
            bg_color=self.themes["app_color"]["dark_two"],
            circle_color=self.themes["app_color"]["icon_color"],
            active_color=self.themes["app_color"]["context_color"]
        )
        self.add_to_myday_layout.addWidget(self.add_to_myday)

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
        self.remind_date_combo.view().pressed.connect(self.handleItemPressed)
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
                "Yearly"
            ]
        )
        self.repeat_task_layout.addWidget(self.repeat_task_combo)

        # ADD TO LIST
        self.add_to_list_frame = QFrame()
        self.add_to_list_layout = QHBoxLayout(self.add_to_list_frame)
        self.add_to_list_layout.setContentsMargins(0, 0, 0, 0)
        self.add_list_label = QLabel()
        self.add_list_label.setText("Add To List:")
        self.add_to_list_layout.addWidget(self.add_list_label)
        self.add_to_list = PyComboBox(
            parent=self.add_to_list_frame,
            data=VAL_LIST
        )
        self.add_to_list.setMinimumHeight(35)
        self.add_to_list_layout.addWidget(self.add_to_list)

        self.layout.addWidget(self.task_name_edit)
        self.layout.addWidget(self.add_to_myday_frame)
        self.layout.addWidget(self.remind_me_frame)
        self.layout.addWidget(self.due_date_frame)
        self.layout.addWidget(self.repeat_task_frame)
        self.layout.addWidget(self.add_to_list_frame)
        self.layout.addWidget(self.save_n_delete_frame)
        self.setLayout(self.layout)

    def function_ui(self):
        self.save_btn.clicked.connect(self.save_changes)
        self.delete_btn.clicked.connect(self.delete_task)

    def save_changes(self):
        self.close()

    def delete_task(self):
        pass

    def extract(self, task_name):
        for row in TASK_DATA:
            if row[1] == task_name:
                self.task_name_edit.setText(row[1])
                self.add_to_myday.setChecked(bool(row[7]))
                self.remind_date_combo.insertItem(0, row[4])
                self.remind_date_combo.setCurrentText(row[4])
                self.remind_me_time.setTime(QTime.fromString(row[5]))
                self.due_date_combo.insertItem(0, row[3])
                self.due_date_combo.setCurrentText(row[3])
                self.repeat_task_combo.insertItem(0, row[6])
                self.repeat_task_combo.setCurrentText(row[6])
                self.add_to_list.setCurrentText(VAL_LIST[KEY_LIST.index(row[11])])

    def handleItemPressed(self, index):
        pass
        # if self.remind_date_combo.currentIndex() == 3:
        #     QDateTimeEdit.calendarPopup(self)
        # print("Do something with the selected item")

