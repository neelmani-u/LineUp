# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

import uuid, os, subprocess, keyboard, re

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
from gui.widgets.py_file_dialog.py_file_dialog import PyFileDialog
from gui.widgets.py_key_sequence_edit.py_key_sequence_edit import PyKeySequenceEdit

# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QLineEdit {{
	background-color: {_bg_color};
	border-radius: {_radius}px;
	border: {_border_size}px solid transparent;
	padding-left: 10px;
    padding-right: 10px;
	selection-color: {_selection_color};
	selection-background-color: {_context_color};
    color: {_color};
    height: 35px;
}}
QLineEdit:focus {{
	border: {_border_size}px solid {_context_color};
    background-color: {_bg_color_active};
}}
'''


class PyHotKeyEditDialog(QDialog):

    def __init__(self):
        super().__init__()

        # SETTINGS
        settings = Settings()
        self.settings = settings.items

        # THEMES
        themes = Themes()
        self.themes = themes.items

        self.setWindowTitle("Edit Hotkeys")
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
        # LAYOUT
        self.layout = QVBoxLayout(self)

        # HOT KEY NAME EDIT
        self.hotkey_name_widget = QWidget()

        # APPLY STYLESHEET
        style_format = style.format(
            _radius=8,
            _border_size=2,
            _color=self.themes["app_color"]["text_foreground"],
            _selection_color=self.themes["app_color"]["white"],
            _bg_color=self.themes["app_color"]["dark_one"],
            _bg_color_active=self.themes["app_color"]["dark_three"],
            _context_color=self.themes["app_color"]["context_color"]
        )

        self.hotkey_name_widget.setStyleSheet(style_format)
        self.hotkey_name_widget_layout = QHBoxLayout(self.hotkey_name_widget)
        self.hotkey_name_widget_layout.setContentsMargins(0, 0, 0, 0)

        self.hotkey_label = QLabel("HotKeys :")
        self.hotkey_name_edit = PyKeySequenceEdit()
        # self.hotkey_name_edit = PyLineEdit(
        #     text="",
        #     place_holder_text="Hotkey",
        #     radius=8,
        #     border_size=2,
        #     color=self.themes["app_color"]["text_foreground"],
        #     selection_color=self.themes["app_color"]["white"],
        #     bg_color=self.themes["app_color"]["dark_one"],
        #     bg_color_active=self.themes["app_color"]["dark_three"],
        #     context_color=self.themes["app_color"]["context_color"]
        # )
        # self.hotkey_name_edit.setMinimumHeight(35)

        self.hotkey_name_widget_layout.addWidget(self.hotkey_label)
        self.hotkey_name_widget_layout.addWidget(self.hotkey_name_edit)

        # HOTKEY ACTION WIDGET
        self.hotkey_action_widget = QWidget()
        self.hotkey_action_widget_layout = QHBoxLayout(self.hotkey_action_widget)
        self.hotkey_action_widget_layout.setContentsMargins(0, 0, 0, 0)

        self.hotkey_action_label = QLabel("Action:")
        self.hotkey_action_combo = PyComboBox(
            parent=self.hotkey_action_widget,
            data=[
                "Open My Computer",
                "Open Notepad",
                "Open Calculator",
                "Reboot Computer",
                "Open Command Prompt"
            ]
        )
        self.hotkey_action_combo.setMinimumHeight(35)

        self.hotkey_action_widget_layout.addWidget(self.hotkey_action_label)
        self.hotkey_action_widget_layout.addWidget(self.hotkey_action_combo)

        # DESTINATION SELECTION
        self.hokey_destination_widget = QWidget()
        self.hokey_destination_widget_layout = QHBoxLayout(self.hokey_destination_widget)
        self.hokey_destination_widget_layout.setContentsMargins(0, 0, 0, 0)

        self.hotkey_destination_label = QLabel("Destination: ")
        self.hotkey_destination_edit = PyLineEdit(
            text="",
            place_holder_text="Path",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.hotkey_destination_edit.setMinimumHeight(35)

        self.hotkey_get_file = PyFileDialog(
            text="Browse",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.hotkey_get_file.setMinimumHeight(35)

        self.hokey_destination_widget_layout.addWidget(self.hotkey_destination_label)
        self.hokey_destination_widget_layout.addWidget(self.hotkey_destination_edit)
        self.hokey_destination_widget_layout.addWidget(self.hotkey_get_file)

        self.save_n_cancel_btn_widget = QWidget()
        self.save_n_cancel_btn_widget_layout = QHBoxLayout(self.save_n_cancel_btn_widget)
        self.save_n_cancel_btn_widget_layout.setContentsMargins(0, 0, 0, 0)

        self.save_btn = PyPushButton(
            text="Save",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.save_btn.setMinimumHeight(35)

        self.cancel_btn = PyPushButton(
            text="Cancel",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.cancel_btn.setMinimumHeight(35)

        self.save_n_cancel_btn_widget_layout.addWidget(self.save_btn)
        self.save_n_cancel_btn_widget_layout.addWidget(self.cancel_btn)

        self.layout.addWidget(self.hotkey_name_widget)
        self.layout.addWidget(self.hotkey_action_widget)
        self.layout.addWidget(self.hokey_destination_widget)
        self.layout.addWidget(self.save_n_cancel_btn_widget)

    def function_ui(self):
        self.save_btn.clicked.connect(self.save_hotkeys_data)
        self.cancel_btn.clicked.connect(self.close)

    def save_hotkeys_data(self):
        hotkey = self.shortcut_customizer(self.get_value_of_hotkey_name_edit())
        hotkey_desc = self.hotkey_action_combo.currentText()
        hotkey_destination = self.hotkey_destination_edit.text()
        Database.add_hotkey(
            Database(),
            hotkey_id=str(uuid.uuid4())[:5],
            hotkey=hotkey,
            hotkey_desc=hotkey_desc,
            hotkey_Destination=hotkey_destination
        )
        self.close()
        self.add_hotkeys_globally(hotkey, hotkey_desc, hotkey_destination)

    def get_value_of_hotkey_name_edit(self):
        sequence = self.hotkey_name_edit.keySequence()
        sequenceString = sequence.toString(QKeySequence.PortableText)
        if sequenceString:
            return sequenceString

    def add_hotkeys_globally(self, hotkey, action, path):
        keyboard.add_hotkey(hotkey.lower(), self.hotkey_action, args=(action, path))
        # keyboard.wait('esc')

    def hotkey_action(self, action, path):
        if action == "Open My Computer":
            subprocess.run(["explorer", ","])
        elif action == "Open Notepad":
            os.system("notepad")
        elif action == "Open Calculator":
            os.system("calc")
        elif action == "Reboot Computer":
            print("System is going to Reboot in 5 min! Press Esc to Cancel")
            # self.showDialog()
        elif action == "Open Command Prompt":
            os.system("start cmd")

    def showDialog(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setText("Do you wish to restart your computer?")
        self.msg.setWindowTitle("Alert!")
        # self.msg.setDetailedText("The details are as follows:")
        self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.msg.buttonClicked.connect(self.reboot)
        retval = self.msg.exec()
        # print(retval)

    def reboot(self, i):
        print(i.text())
        # os.system("shutdown /r /t 1")

    def shortcut_customizer(self, shortcut):
        pat = re.compile(r"([+])")
        pat.sub(" \\1 ", shortcut)
        return shortcut.lower()
