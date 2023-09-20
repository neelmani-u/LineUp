# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
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
from gui.core.json_themes import Themes
from gui.core.json_settings import Settings
import uuid

# STYLE
# ///////////////////////////////////////////////////////////////
style = "border: none;"


class PyLinkManager(QWidget):
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
        # LINK MANAGER APP LAYOUT
        self.link_manager_layout = QHBoxLayout(self)
        self.link_manager_layout.setContentsMargins(0, 0, 0, 0)
        self.link_manager_layout.setSpacing(10)

        # CATEGORY WIDGETS
        self.left_widget = QWidget()
        self.left_widget.setMaximumWidth(300)
        self.left_widget_layout = QVBoxLayout(self.left_widget)
        self.left_widget_layout.setContentsMargins(0, 0, 0, 0)

        self.category_label_le_widget = QWidget()
        self.category_label_le_widget_layout = QHBoxLayout(self.category_label_le_widget)
        self.category_label_le_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.category_label = QLabel("Category:")
        self.category_line_edit = PyLineEdit(
            text="",
            place_holder_text="Category Name",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.category_line_edit.setMinimumHeight(35)
        self.category_label_le_widget_layout.addWidget(self.category_label)
        self.category_label_le_widget_layout.addWidget(self.category_line_edit)

        self.left_box_add_replace_btn_widget = QWidget()
        self.left_box_add_replace_btn_widget_layout = QHBoxLayout(self.left_box_add_replace_btn_widget)
        self.left_box_add_replace_btn_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.left_box_add_btn = PyPushButton(
            text="Add",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.left_box_add_btn.setMinimumHeight(35)
        self.left_box_replace_btn = PyPushButton(
            text="Replace",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.left_box_replace_btn.setMinimumHeight(35)
        self.left_box_add_replace_btn_widget_layout.addWidget(self.left_box_add_btn)
        self.left_box_add_replace_btn_widget_layout.addWidget(self.left_box_replace_btn)

        self.category_list_view = PyListWidget(
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["context_color"],
            bg_color=self.themes["app_color"]["bg_two"],
            bottom_line_color=self.themes["app_color"]["bg_three"],
            grid_line_color=self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color=self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color=self.themes["app_color"]["dark_four"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.link_category_data = Database.get_link_category(Database())
        for data in self.link_category_data:
            self.category_list_view.addItem(data[1])

        self.left_widget_layout.addWidget(self.category_label_le_widget)
        self.left_widget_layout.addWidget(self.left_box_add_replace_btn_widget)
        self.left_widget_layout.addWidget(self.category_list_view)

        # SELECTED CATEGORY WIDGETS
        self.right_widget = QWidget()
        self.right_widget_layout = QVBoxLayout(self.right_widget)
        self.right_widget_layout.setContentsMargins(0, 0, 0, 0)

        self.right_link_name_edit = QWidget()
        self.right_link_name_edit_layout = QHBoxLayout(self.right_link_name_edit)
        self.right_link_name_edit_layout.setContentsMargins(0, 0, 0, 0)
        self.right_link_name = QLabel("Name :")
        self.right_link_line_edit = PyLineEdit(
            text="",
            place_holder_text="Link Name",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.right_link_line_edit.setMinimumHeight(35)
        self.right_box_link_add_btn = PyPushButton(
            text="      Add      ",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.right_box_link_add_btn.setMinimumHeight(35)
        self.right_link_name_edit_layout.addWidget(self.right_link_name)
        self.right_link_name_edit_layout.addWidget(self.right_link_line_edit)
        self.right_link_name_edit_layout.addWidget(self.right_box_link_add_btn)

        self.right_link_url_edit = QWidget()
        self.right_link_url_edit_layout = QHBoxLayout(self.right_link_url_edit)
        self.right_link_url_edit_layout.setContentsMargins(0, 0, 0, 0)
        self.right_url_name = QLabel("URL :    ")
        self.right_url_line_edit = PyLineEdit(
            text="",
            place_holder_text="Link URL",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.right_url_line_edit.setMinimumHeight(35)
        self.right_box_link_replace_btn = PyPushButton(
            text="   Replace   ",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.right_box_link_replace_btn.setMinimumHeight(35)
        self.right_link_url_edit_layout.addWidget(self.right_url_name)
        self.right_link_url_edit_layout.addWidget(self.right_url_line_edit)
        self.right_link_url_edit_layout.addWidget(self.right_box_link_replace_btn)

        self.link_table_view = PyTableWidget(
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
        self.link_table_view.setColumnCount(2)
        self.link_table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.link_table_view.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.link_table_view.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Columns / Header

        self.name_column = QTableWidgetItem()
        self.name_column.setTextAlignment(Qt.AlignCenter)
        self.name_column.setText("NAME")

        self.url_column = QTableWidgetItem()
        self.url_column.setTextAlignment(Qt.AlignCenter)
        self.url_column.setText("URL")

        # Set column
        self.link_table_view.setHorizontalHeaderItem(0, self.name_column)
        self.link_table_view.setHorizontalHeaderItem(1, self.url_column)

        self.right_widget_layout.addWidget(self.right_link_name_edit)
        self.right_widget_layout.addWidget(self.right_link_url_edit)
        self.right_widget_layout.addWidget(self.link_table_view)

        # ADD WIDGETS TO LINK MANAGER APP LAYOUT
        self.link_manager_layout.addWidget(self.left_widget)
        self.link_manager_layout.addWidget(self.right_widget)

    def function_ui(self):
        self.left_box_add_btn.clicked.connect(self.add_category_list)
        self.left_box_replace_btn.clicked.connect(self.update_category_list)
        self.right_box_link_add_btn.clicked.connect(self.add_link_in_table)
        self.right_box_link_replace_btn.clicked.connect(self.update_link_table)
        self.category_list_view.itemDoubleClicked.connect(self.clicked_on)

    def add_category_list(self):
        category = self.category_line_edit.text()
        category_list = Database.get_link_category(Database())
        if not category:
            pass
        elif category not in category_list:
            Database.add_link_category(
                Database(),
                category_id=str(uuid.uuid4())[:4],
                category_name=category
            )
            self.category_list_view.addItem(category)
        self.category_line_edit.clear()

    def update_category_list(self):
        category = self.category_line_edit.text()
        category_list = Database.get_link_category(Database())
        category_id = self.find_category_id(self.category_list_view.currentItem().text())
        if not category:
            pass
        elif category not in category_list:
            Database.update_link_category(
                Database(),
                category_id=category_id,
                category_name=category
            )
            self.category_list_view.currentItem().setText(category)
        self.category_line_edit.clear()

    def add_link_in_table(self):
        link_name = self.right_link_line_edit.text()
        link_url = self.right_url_line_edit.text()
        category_id = self.find_category_id(self.category_list_view.currentItem().text())
        if not link_name:
            pass
        elif not link_url:
            pass
        else:
            Database.add_link_book(
                Database(),
                link_book_id=str(uuid.uuid4())[:6],
                link_name=link_name,
                link_url=link_url,
                link_category_id=category_id
            )
            self.add_item_in_table_view(link_name, link_url)
        self.right_link_line_edit.clear()
        self.right_url_line_edit.clear()

    def update_link_table(self):
        link_name = self.right_link_line_edit.text()
        link_url = self.right_url_line_edit.text()
        link_book_id = self.find_link_book_id(self.link_table_view.currentItem().text())
        category_id = self.find_category_id(self.category_list_view.currentItem().text())
        if not link_name:
            pass
        elif not link_url:
            pass
        else:
            Database.update_link_book(
                Database(),
                link_book_id=link_book_id,
                link_name=link_name,
                link_url=link_url,
                link_category_id=category_id
            )
            self.add_item_in_table_view(link_name, link_url, self.link_table_view.currentRow())
        self.right_link_line_edit.clear()
        self.right_url_line_edit.clear()

    def clicked_on(self):
        self.link_table_view.setRowCount(0)
        self.link_book_data = Database.get_link_book(Database())
        self.link_category_data = Database.get_link_category(Database())
        category_id = self.find_category_id(self.category_list_view.currentItem().text())
        self.specific_link_book_data = Database.get_link_details_by_category(Database(), category_id)
        if not self.specific_link_book_data:
            self.link_table_view.setRowCount(0)
        else:
            for data in self.specific_link_book_data:
                self.add_item_in_table_view(data[1], data[2])

    def find_category_id(self, itm):
        for sub_list in self.link_category_data:
            if itm in sub_list:
                return sub_list[0]
        raise ValueError("'{itm}' is not in list".format(itm=itm))

    def find_link_book_id(self, itm):
        for sub_list in self.link_book_data:
            if itm in sub_list:
                return sub_list[0]
        raise ValueError("'{itm}' is not in list".format(itm=itm))

    def add_item_in_table_view(self, col_0, col_1, row=None):
        if row is None:
            row = self.link_table_view.rowCount()
            self.link_table_view.insertRow(row)
        self.link_table_view.setItem(row, 0, QTableWidgetItem(col_0))
        self.link_table_view.setItem(row, 1, QTableWidgetItem(col_1))
        self.link_table_view.setRowHeight(row, 22)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Delete:
            self.delete_item()

    def delete_item(self):
        if self.category_list_view.hasFocus():
            idx = self.category_list_view.currentRow()
            category_id = self.find_category_id(self.category_list_view.currentItem().text())
            Database.delete_link_category_row(Database(), category_id)
            self.category_list_view.takeItem(idx)
        elif self.link_table_view.hasFocus():
            row = self.link_table_view.currentRow()
            link_book_id = self.find_link_book_id(self.link_table_view.currentItem().text())
            Database.delete_link_book_row(Database(), link_book_id)
            self.link_table_view.removeRow(row)
