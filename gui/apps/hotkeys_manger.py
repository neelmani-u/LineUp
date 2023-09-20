from qt_core import *

# IMPORT DB CORE
# ///////////////////////////////////////////////////////////////
from db_core import *

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.widgets.py_list_widget.py_list_widget import PyListWidget
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from gui.widgets.py_push_button.py_push_button import PyPushButton
from gui.widgets.py_line_edit.py_line_edit import PyLineEdit
from gui.widgets.py_icon_button.py_icon_button import PyIconButton
from gui.widgets.py_hotkey_edit_dialog.py_hotkey_edit_dialog import PyHotKeyEditDialog
from gui.core.json_themes import Themes
from gui.core.json_settings import Settings

# STYLE
# ///////////////////////////////////////////////////////////////
style = "border: none;"


class PyHotKeysManager(QWidget):
    def __init__(
            self,
            parent=None
    ):
        super().__init__()

        # THEME
        themes = Themes()
        self.themes = themes.items

        # SETTINGS
        settings = Settings()
        self.settings = settings.items

        # SETUP UI
        self.setup_ui()

        # FUNCTION UI
        self.function_ui()

        # PARENT
        if parent != None:
            self.setParent(parent)

    def setup_ui(self):

        # HOTKEY LAYOUT
        self.hotkeys_manager_layout = QVBoxLayout(self)
        self.hotkeys_manager_layout.setContentsMargins(0, 0, 0, 0)

        # TABLE WIDGETS
        self.hotkeys_table_view = PyTableWidget(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["context_color"],
            bg_color=self.themes["app_color"]["bg_two"],
            header_horizontal_color=self.themes["app_color"]["dark_two"],
            header_vertical_color=self.themes["app_color"]["bg_three"],
            bottom_line_color=self.themes["app_color"]["bg_three"],
            grid_line_color=self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            context_color=self.themes["app_color"]["context_color"]
        )

        self.hotkeys_table_view.setColumnCount(3)
        self.hotkeys_table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.hotkeys_table_view.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.hotkeys_table_view.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Columns / Header
        self.hotkey_column = QTableWidgetItem()
        self.hotkey_column.setTextAlignment(Qt.AlignCenter)
        self.hotkey_column.setText("Hotkey")

        self.desc_column = QTableWidgetItem()
        self.desc_column.setTextAlignment(Qt.AlignCenter)
        self.desc_column.setText("Description")

        self.destination_column = QTableWidgetItem()
        self.destination_column.setTextAlignment(Qt.AlignCenter)
        self.destination_column.setText("Destination")

        # Set column
        self.hotkeys_table_view.setHorizontalHeaderItem(0, self.hotkey_column)
        self.hotkeys_table_view.setHorizontalHeaderItem(1, self.desc_column)
        self.hotkeys_table_view.setHorizontalHeaderItem(2, self.destination_column)

        # ADD DATA
        hotkey_data = Database.get_hotkey_details(Database())
        for itm in hotkey_data:
            self.add_item_in_hotkey_table_view(itm[1], itm[2], itm[3])

        # BUTTONS WIDGETS
        self.btn_widgets = QWidget()
        self.btn_widgets_layout = QHBoxLayout(self.btn_widgets)
        self.btn_widgets_layout.setContentsMargins(0, 0, 0, 0)

        # ADD BTN
        self.add_btn = PyPushButton(
            text="Add",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.add_btn.setMinimumHeight(35)

        # EDIT BTN
        self.edit_btn = PyPushButton(
            text="Edit",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.edit_btn.setMinimumHeight(35)

        # DELETE BTN
        self.delete_btn = PyPushButton(
            text="Delete",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.delete_btn.setMinimumHeight(35)

        # DELETE ALL
        self.delete_all_btn = PyPushButton(
            text="Delete All",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.delete_all_btn.setMinimumHeight(35)

        # ADD BTN WIDGETS TO BTN LAYOUT
        self.btn_widgets_layout.addWidget(self.add_btn)
        self.btn_widgets_layout.addWidget(self.edit_btn)
        self.btn_widgets_layout.addWidget(self.delete_btn)
        self.btn_widgets_layout.addWidget(self.delete_all_btn)

        # ADD TABLE AND BTN WIDGET TO HOTKEY MANAGER LAYOUT
        self.hotkeys_manager_layout.addWidget(self.hotkeys_table_view)
        self.hotkeys_manager_layout.addWidget(self.btn_widgets)

    def function_ui(self):
        self.add_btn.clicked.connect(self.add_hotkeys)
        self.edit_btn.clicked.connect(self.edit_hotkeys)
        self.delete_btn.clicked.connect(self.delete_hotkeys)
        self.delete_all_btn.clicked.connect(self.delete_all_hotkeys)

    def add_hotkeys(self):
        self.dialog = PyHotKeyEditDialog()
        self.dialog.exec_()
        self.update_table()

    def update_table(self):
        hotkey_data = Database.get_hotkey_details(Database())
        table_row = self.hotkeys_table_view.rowCount()
        if len(hotkey_data) > table_row:
            for itm in hotkey_data[table_row:]:
                self.add_item_in_hotkey_table_view(itm[1], itm[2], itm[3])

    def edit_hotkeys(self):
        selected = self.hotkeys_table_view.selectedItems()
        self.dialog = PyHotKeyEditDialog()
        self.dialog.hotkey_action_combo.setCurrentText(selected[1].text())
        self.dialog.hotkey_destination_edit.setText(selected[2].text())
        self.dialog.exec_()

    def delete_hotkeys(self):
        row = self.hotkeys_table_view.currentRow()
        hotkey_data = Database.get_hotkey_details(Database())
        hotkey_id = hotkey_data[row-1][0]
        Database.delete_hotkey(Database(), hotkey_id)
        self.hotkeys_table_view.removeRow(row)

    def delete_all_hotkeys(self):
        Database.delete_all_hotkeys(Database())
        self.hotkeys_table_view.setRowCount(0)

    def add_item_in_hotkey_table_view(self, col_0, col_1, col_2, row=None):
        if row is None:
            row = self.hotkeys_table_view.rowCount()
            self.hotkeys_table_view.insertRow(row)
        self.hotkeys_table_view.setItem(row, 0, QTableWidgetItem(col_0))
        self.hotkeys_table_view.setItem(row, 1, QTableWidgetItem(col_1))
        self.hotkeys_table_view.setItem(row, 2, QTableWidgetItem(col_2))
        self.hotkeys_table_view.setRowHeight(row, 22)

