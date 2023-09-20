# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT DB CORE
# ///////////////////////////////////////////////////////////////
from db_core import *

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.widgets.py_tab_widget.py_tab_widget import PyTabWidget
from gui.widgets.py_create_task_expandable.py_create_task import PyCreateTask
from gui.widgets.py_create_list_expandable.py_create_list import PyCreateList
from gui.widgets.py_task_button.py_task_button import PyTaskButton
from gui.widgets.py_myday_task.py_myday_task_remaining import PyTaskRemaining
from gui.widgets.py_myday_task.py_myday_task_completed import PyTaskCompleted
from gui.widgets.py_lists.py_lists import PyLists
from gui.core.json_themes import Themes
from gui.core.json_settings import Settings

# STYLE
# ///////////////////////////////////////////////////////////////
style = "border: none;"


class PyTaskManager(QWidget):
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
        self.setup_ui(parent)

        # FUNCTION UI
        self.function_ui()

        # PARENT
        # if parent != None:
        #     self.setParent(parent)

    def setup_ui(self, parent):
        # PAGE 2
        self.task_manager_page_layout = QVBoxLayout(self)
        self.task_manager_page_layout.setContentsMargins(0, 0, 0, 0)
        self.task_tab_widget = PyTabWidget(
            radius=8,
            bg_color=self.themes["app_color"]["bg_one"],
            # selection_color=self.themes["app_color"]["context_color"],
            selection_color=self.themes["app_color"]["dark_one"],
            parent=parent
        )
        # self.task_tab_scroll = QScrollArea()
        self.task_create_tab = QWidget(self.task_tab_widget)
        self.task_create_tab_layout = QVBoxLayout(self.task_create_tab)
        self.task_create_tab_layout.setContentsMargins(5, 5, 5, 5)
        self.create_task_btn = PyCreateTask(
            parent=self.task_create_tab
        )

        self.create_list_btn = PyCreateList(
            parent=self.task_create_tab
        )

        # self.create_group_btn = PyCreateGroup(
        #     parent=self.task_create_tab
        # )

        self.task_create_tab_layout.addWidget(self.create_task_btn)
        self.task_create_tab_layout.addWidget(self.create_list_btn)
        # self.task_create_tab_layout.addWidget(self.create_group_btn)
        self.task_create_tab_layout.setAlignment(Qt.AlignTop)

        # self.task_tab_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.task_tab_scroll.setWidgetResizable(True)
        # self.task_tab_scroll.setWidget(self.task_create_tab)
        self.task_tab_widget.addTab(self.task_create_tab, "Create")

        self.task_myday_tab = QWidget(self.task_tab_widget)
        self.myday_tab_layout = QVBoxLayout(self.task_myday_tab)
        self.task_myday_tab_scroll_area = QScrollArea()
        self.task_myday_tab_scroll_area.setStyleSheet(style)
        self.task_myday_tab_scroll_area.setParent(self.task_myday_tab)
        self.myday_widget = QWidget()
        self.task_myday_tab_layout = QVBoxLayout()
        self.task_myday_tab_layout.setContentsMargins(0, 0, 0, 0)
        self.task_myday_tab_layout.setSpacing(5)
        self.myday_widget.setLayout(self.task_myday_tab_layout)
        self.task_myday_tab_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.task_myday_tab_scroll_area.setWidgetResizable(True)
        self.task_myday_tab_scroll_area.setWidget(self.myday_widget)
        self.task_remaining = PyTaskRemaining(
            parent=self.task_myday_tab
        )
        self.task_completed = PyTaskCompleted(
            parent=self.task_myday_tab
        )
        self.task_myday_tab_layout.addWidget(self.task_remaining)
        self.task_myday_tab_layout.addWidget(self.task_completed)
        self.task_myday_tab_layout.setAlignment(Qt.AlignTop)
        self.myday_tab_layout.addWidget(self.task_myday_tab_scroll_area, 0, Qt.AlignTop)
        self.task_tab_widget.addTab(self.task_myday_tab, "My Day")

        self.task_tasks_tab = QWidget(self.task_tab_widget)
        self.tasks_tab_layout = QVBoxLayout(self.task_tasks_tab)
        self.task_tasks_tab_scroll_area = QScrollArea()
        self.task_tasks_tab_scroll_area.setStyleSheet(style)
        self.task_tasks_tab_scroll_area.setParent(self.task_tasks_tab)
        self.widget = QWidget()
        self.task_tasks_tab_layout = QVBoxLayout()
        self.task_tasks_tab_layout.setContentsMargins(0, 0, 0, 0)
        self.task_tasks_tab_layout.setSpacing(2)
        self.widget.setLayout(self.task_tasks_tab_layout)
        self.task_tasks_tab_layout.setAlignment(Qt.AlignTop)
        self.task_tasks_tab_scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.task_tasks_tab_scroll_area.setWidgetResizable(True)
        self.task_tasks_tab_scroll_area.setWidget(self.widget)
        self.task_tasks_tab_scroll_area.setAlignment(Qt.AlignTop)
        for row in TASK_DATA:
            if row[9] != 1:
                self.task_btn = PyTaskButton(
                    parent=self.task_tasks_tab_scroll_area,
                    task_id=row[0],
                    task_name=row[1]
                )
                self.task_tasks_tab_layout.addWidget(self.task_btn)
        # self.task_tasks_tab_layout.setAlignment(Qt.AlignTop)
        self.task_tab_completed = PyTaskCompleted(
            parent=self.task_tasks_tab_scroll_area
        )
        self.task_tab_completed.setMinimumHeight(250)
        self.task_tasks_tab_layout.setAlignment(Qt.AlignTop)
        self.tasks_tab_layout.addWidget(self.task_tasks_tab_scroll_area)
        self.task_tasks_tab_layout.addWidget(self.task_tab_completed)
        # self.tasks_tab_layout.addWidget(self.task_tab_completed)
        self.task_tab_widget.addTab(self.task_tasks_tab, "Tasks")

        self.task_lists_tab = QWidget(self.task_tab_widget)
        self.task_lists_tab_layout = QVBoxLayout(self.task_lists_tab)
        self.task_lists_tab_layout.setContentsMargins(5, 5, 5, 5)
        self.task_lists = PyLists(
            parent=self.task_lists_tab
        )
        self.task_lists_tab_layout.addWidget(self.task_lists)
        self.task_lists_tab_layout.setAlignment(Qt.AlignTop)
        self.task_tab_widget.addTab(self.task_lists_tab, "Lists")

        # self.task_groups_tab = QWidget(self.task_tab_widget)
        # self.task_tab_widget.addTab(self.task_groups_tab, "Groups")
        self.task_manager_page_layout.addWidget(self.task_tab_widget)

    def function_ui(self):
        self.task_tab_widget.currentChanged.connect(self.update_tab)

    def update_tab(self):
        rem_task_data = Database.get_myday_task_details(Database(), today, 0)
        self.update_my_day_tab(rem_task_data)
        self.update_task_tab()
        self.update_list_tab()

    def update_task_tab(self):
        task_data = Database.get_task_details(Database(), is_sort=True)
        self.task_tasks_tab_layout.removeWidget(self.task_tab_completed)
        for row in task_data:
            if row not in TASK_DATA:
                if row[9] != 1:
                    TASK_DATA.append(row)
                    self.task_btn = PyTaskButton(
                        parent=self.task_tasks_tab_scroll_area,
                        task_id=row[0],
                        task_name=row[1]
                    )
                    self.task_tasks_tab_layout.addWidget(self.task_btn)
                elif row[9] == 1:
                    items = [self.task_tasks_tab_layout.itemAt(i).widget() for i in
                             range(self.task_tasks_tab_layout.count())]
                    for w in items:
                        if w.objectName() == row[0]:
                            self.task_tasks_tab_layout.removeWidget(w)
                            self.task_remaining.myday_task_view_scroll_area_layout.removeWidget(w)
                            self.task_tab_completed.TASK_COMPLETED = self.task_tab_completed.TASK_COMPLETED + 1
                            self.task_tab_completed.MAXIMUM_HEIGHT = 45 * self.task_tab_completed.TASK_COMPLETED
                            self.task_tab_completed.myday_task_view_scroll_area_layout.setMaximumHeight(self.task_tab_completed.MAXIMUM_HEIGHT)
                            self.task_tab_completed.myday_task_view_scroll_area_layout.addWidget(w)
        self.task_tasks_tab_layout.addWidget(self.task_tab_completed)

    def update_my_day_tab(self, rem_task_data):
        print(rem_task_data)
        for row in rem_task_data:
            if row not in REMAINING_TASK_DATA:
                if row[9] != 1:
                    print(row)
                    print(type(row))
                    print(row[3] == today)
                    REMAINING_TASK_DATA.append(row)
                    self.task_remaining.setup_task_buttons([row])
                    # for idx in range(self.task_remaining.myday_task_view_scroll_area_layout.count()):
                    #     itm = self.task_remaining.myday_task_view_scroll_area_layout.itemAt(idx)
                    #     if itm.widget().objectName() == row[0]:
                    #         itm_list.append(itm)
        # for itm in itm_list:
        #     if itm is not None:
        #         PyTaskRemaining.TASK_REMAINING = PyTaskRemaining.TASK_REMAINING - 1
        #         PyTaskRemaining.MAXIMUM_HEIGHT = 45 * PyTaskRemaining.TASK_REMAINING
        #         self.task_remaining.widget.setMaximumHeight(PyTaskRemaining.MAXIMUM_HEIGHT)
        #
        #         # itm.widget().setParent(self.task_completed.myday_task_view_scroll_area)
        #         PyTaskCompleted.TASK_COMPLETED = PyTaskCompleted.TASK_COMPLETED + 1
        #         PyTaskCompleted.MAXIMUM_HEIGHT = 45 * PyTaskCompleted.TASK_COMPLETED
        #         self.task_completed.widget.setMaximumHeight(PyTaskCompleted.MAXIMUM_HEIGHT)
        #         self.task_completed.myday_task_view_scroll_area_layout.addItem(itm)
        #         self.task_tab_completed.myday_task_view_scroll_area_layout.addItem(itm)

        for row in rem_task_data:
            if row not in REMAINING_TASK_DATA:
                REMAINING_TASK_DATA.append(row)
                PyTaskRemaining.TASK_REMAINING = PyTaskRemaining.TASK_REMAINING + 1
                PyTaskRemaining.MAXIMUM_HEIGHT = 45 * PyTaskRemaining.TASK_REMAINING
                self.task_remaining.widget.setMaximumHeight(PyTaskRemaining.MAXIMUM_HEIGHT)
                self.task_btn = PyTaskButton(
                    parent=self.task_remaining.myday_task_view_scroll_area,
                    task_id=row[0],
                    task_name=row[1]
                )
                self.task_remaining.myday_task_view_scroll_area_layout.addWidget(self.task_btn)

    def update_myday_tab(self):
        rem_task_data = Database.get_myday_task_details(Database(), today, 0)
        # no_of_old_rem_td = len(REMAINING_TASK_DATA)
        # no_of_new_rem_td = len(rem_task_data)
        for row in rem_task_data:
            if row not in REMAINING_TASK_DATA:
                REMAINING_TASK_DATA.append(row)
                PyTaskRemaining.TASK_REMAINING = PyTaskRemaining.TASK_REMAINING + 1
                PyTaskRemaining.MAXIMUM_HEIGHT = 45 * PyTaskRemaining.TASK_REMAINING
                self.task_remaining.widget.setMaximumHeight(PyTaskRemaining.MAXIMUM_HEIGHT)
                self.task_btn = PyTaskButton(
                    parent=self.task_remaining.myday_task_view_scroll_area,
                    task_id=row[0],
                    task_name=row[1]
                )
                self.task_remaining.myday_task_view_scroll_area_layout.addWidget(self.task_btn)
        # if not no_of_old_rem_td == no_of_new_rem_td:
        #     REMAINING_TASK_DATA.append(rem_task_data[len(REMAINING_TASK_DATA)])
        #     self.task_btn = PyTaskButton(
        #         parent=self.task_remaining.myday_task_view_scroll_area,
        #         task_name=REMAINING_TASK_DATA[-1][1]
        #     )
        #     self.task_remaining.myday_task_view_scroll_area_layout.addWidget(self.task_btn)

        com_task_data = Database.get_myday_task_details(Database(), today, 1)
        # no_of_old_com_td = len(COMPLETED_TASK_DATA)
        # no_of_new_com_td = len(com_task_data)
        for row in com_task_data:
            if row not in COMPLETED_TASK_DATA:
                COMPLETED_TASK_DATA.append(row)
                PyTaskCompleted.TASK_COMPLETED = PyTaskCompleted.TASK_COMPLETED + 1
                PyTaskCompleted.MAXIMUM_HEIGHT = 45 * PyTaskCompleted.TASK_COMPLETED
                self.task_completed.widget.setMaximumHeight(PyTaskCompleted.MAXIMUM_HEIGHT)
                self.task_btn = PyTaskButton(
                    parent=self.task_completed.myday_task_view_scroll_area,
                    task_id=row[0],
                    task_name=row[1],
                    is_tick=bool(row[9]),
                    is_star=bool(row[10])
                )
                self.task_completed.myday_task_view_scroll_area_layout.addWidget(self.task_btn)

    # def update_task_tab(self):
    #     task_data = Database.get_task_details(Database(), is_sort=True)
    #

    def update_list_tab(self):
        pass
