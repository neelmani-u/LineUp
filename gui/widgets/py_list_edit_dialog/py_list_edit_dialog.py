# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings
from gui.core.json_themes import Themes
from qt_core import *

from gui.widgets import PyPushButton, PyLineEdit
from gui.widgets.py_check_combo_box.py_check_combo_box import PyCheckComboBox


class PyListEditDialog(QDialog):

    def __init__(self):
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

    def setup_ui(self):
        # TASK NAME EDIT
        self.list_name_edit = PyLineEdit(
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
        self.list_name_edit.setMinimumHeight(35)

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

        # ADD TO LIST
        self.add_list_to_task_frame = QFrame()
        self.add_to_list_layout = QHBoxLayout(self.add_list_to_task_frame)
        self.add_to_list_layout.setContentsMargins(0, 0, 0, 0)
        self.add_list_label = QLabel()
        self.add_list_label.setText("Add To List:")
        self.add_to_list_layout.addWidget(self.add_list_label)
        self.add_to_list = PyCheckComboBox(
            parent=self.add_list_to_task_frame,
            data=[
                "Task 1",
                "Task 2"
            ]
        )
        self.add_to_list.setMinimumHeight(35)
        self.add_to_list_layout.addWidget(self.add_to_list)

        self.layout.addWidget(self.list_name_edit)
        self.layout.addWidget(self.add_list_to_task_frame)
        self.layout.addWidget(self.save_n_delete_frame)
        self.setLayout(self.layout)

    def function_ui(self):
        self.save_btn.clicked.connect(self.save_changes)
        self.delete_btn.clicked.connect(self.delete_task)

    def save_changes(self):
        self.close()

    def delete_task(self):
        pass

    def handleItemPressed(self, index):
        pass
        # if self.remind_date_combo.currentIndex() == 3:
        #     QDateTimeEdit.calendarPopup(self)
        # print("Do something with the selected item")