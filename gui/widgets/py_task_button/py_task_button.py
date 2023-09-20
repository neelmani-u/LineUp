# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT DB CORE
# ///////////////////////////////////////////////////////////////
from db_core import *

from gui.core.json_themes import Themes
from gui.uis.windows.main_window.functions_main_window import Functions
from gui.widgets.py_icon_button.py_icon_button import PyIconButton
from gui.widgets.py_push_button.py_push_button import PyPushButton
from gui.widgets.py_task_edit_dialog.py_task_edit_dialog import PyTaskEditDialog


class PyTaskButton(QWidget):
    TICK = False
    STAR = False

    def __init__(
            self,
            task_id=None,
            task_name="Task Name",
            is_tick=False,
            is_star=False,
            parent=None
    ):
        super().__init__()

        # MAKE UNIQUE EACH TASK BY SETTING ID
        if task_id != None:
            self.setObjectName(task_id)

        # THEME
        themes = Themes()
        self.themes = themes.items

        # SETUP UI
        self.setup_ui(task_name, is_tick, is_star)

        # FUNCTION UI
        self.function_ui()

        # PARENT
        if parent != None:
            self.setParent(parent)

    def setup_ui(self, tn, tck, st):
        # ADD LAYOUT
        self.task_btn_layout = QHBoxLayout(self)
        self.task_btn_layout.setContentsMargins(2, 2, 2, 2)
        self.task_btn_layout.setSpacing(2)

        # TICK BUTTON
        self.tick_btn = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_task_untick.svg"),
            # parent=mpt,
            # tooltip_text="Mark Completed",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            # icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            is_active=PyTaskButton.TICK
        )
        if tck:
            PyTaskButton.TICK = tck
            self.tick_btn.set_icon(Functions.set_svg_icon("icon_task_tick.svg"))

        # TASK NAME BUTTON
        self.task_name_btn = PyPushButton(
            text=tn,
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.task_name_btn.setMinimumHeight(40)

        # STAR BUTTON
        self.task_star_btn = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_unstar.svg"),
            # parent=mpt,
            # tooltip_text="Mark Important",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            is_active=PyTaskButton.STAR
        )
        if st:
            PyTaskButton.STAR = st
            self.task_star_btn.set_icon(Functions.set_svg_icon("icon_star.svg"))

        # ADD WIDGETS
        self.task_btn_layout.addWidget(self.tick_btn)
        self.task_btn_layout.addWidget(self.task_name_btn)
        self.task_btn_layout.addWidget(self.task_star_btn)

    def function_ui(self):
        self.tick_btn.clicked.connect(self.ticked)
        self.task_name_btn.clicked.connect(self.task_info)
        self.task_star_btn.clicked.connect(self.starred)

    def ticked(self):
        if PyTaskButton.TICK:
            PyTaskButton.TICK = False
            self.tick_btn.set_icon(Functions.set_svg_icon("icon_task_untick.svg"))
            for row in TASK_DATA:
                if self.task_name_btn.text() == row[1]:
                    Database.update_task_status(Database(), row[0], 0)
            # self.tick_btn.set_active(PyTaskButton.TICK)
        else:
            PyTaskButton.TICK = True
            self.tick_btn.set_icon(Functions.set_svg_icon("icon_task_tick.svg"))
            for row in TASK_DATA:
                if self.task_name_btn.text() == row[1]:
                    Database.update_task_status(Database(), row[0], 1)
            # self.tick_btn.set_active(PyTaskButton.TICK)

    def starred(self):
        if PyTaskButton.STAR:
            PyTaskButton.STAR = False
            self.task_star_btn.set_icon(Functions.set_svg_icon("icon_unstar.svg"))
            for row in TASK_DATA:
                if self.task_name_btn.text() == row[1]:
                    Database.update_task_important(Database(), row[-2], 0)
            # self.task_star_btn.set_active(PyTaskButton.STAR)
        else:
            PyTaskButton.STAR = True
            self.task_star_btn.set_icon(Functions.set_svg_icon("icon_star.svg"))
            for row in TASK_DATA:
                if self.task_name_btn.text() == row[1]:
                    Database.update_task_important(Database(), row[-2], 1)
            # self.task_star_btn.set_active(PyTaskButton.STAR)

    def task_info(self):
        task_name = self.task_name_btn.text()
        self.dialog = PyTaskEditDialog(task_name)
        self.dialog.exec_()
        # self.dialog = QDialog(self)
        # self.dialog.setWindowTitle("Task Edit")
        # self.dialog.exec_()
        # self.d = CustomDialog()
        # self.d.exec_()
