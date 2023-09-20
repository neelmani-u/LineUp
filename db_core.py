# DB CORE
# ///////////////////////////////////////////////////////////////
from gui.core.database import Database

from datetime import date


today = date.today().strftime("%d/%m/%y")
TASK_DATA = Database.get_task_details(Database())
MY_DAY_TASK_DATA = Database.get_myday_task_details(Database(), today, None)
REMAINING_TASK_DATA = Database.get_myday_task_details(Database(), today, 0)
COMPLETED_TASK_DATA = Database.get_myday_task_details(Database(), today, 1)
LIST_DATA = dict(Database.get_list_details(Database()))
KEY_LIST = list(LIST_DATA.keys())
KEY_LIST.insert(0, "None")
VAL_LIST = list(LIST_DATA.values())
VAL_LIST.insert(0, "None")
TASK_NAMES = [row[1] for row in TASK_DATA]

# print(TASK_DATA)

