# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import sys, pathlib
import sqlite3


# APP DATABASE
# ///////////////////////////////////////////////////////////////
class Database:
    def __init__(self):
        # EXISTS
        file_path = pathlib.Path("lineupDb.sqlite3")
        exists = file_path.is_file()
        # print(exists)

        # CONNECTION
        self.con = sqlite3.connect("lineupDb.sqlite3")
        self.cursor = self.con.cursor()
        # if not con.open():
        #     QMessageBox.critical(
        #         None,
        #         "App Name - Error",
        #         "Database Error: %s" % con.lastError().databaseText(),
        #         )
        #     sys.exit(1)
        # else:
        #     win = QLabel("Connection Successfully Opened!")
        #     win.resize(200, 100)
        #     win.show()

        # VERIFY
        if not exists:
            self.setup_tables()
        # con.close()

    def setup_tables(self):
        self.cursor.execute(
            """
            CREATE TABLE list_details (
                list_id VARCHAR2(5) PRIMARY KEY NOT NULL,
                list_name VARCHAR2(200) NOT NULL
            )
            """
        )
        self.con.commit()

        self.cursor.execute(
            """
            CREATE TABLE task_details (
                task_id VARCHAR2(5) PRIMARY KEY NOT NULL,
                task_name VARCHAR2(200) NOT NULL,
                created_date DATE NOT NULL,
                due_date DATE,
                remind_date DATE,
                remind_time TIME,
                repeat DATE,
                my_day BOOLEAN,
                priority_lvl VARCHAR2(50),
                status BOOLEAN,
                important BOOLEAN,
                list_id VARCHAR2(5),
                FOREIGN KEY (list_id) REFERENCES list_details(list_id)
            )
            """
        )
        self.con.commit()

        self.cursor.execute(
            """
            CREATE TABLE link_category(
                category_id VARCHAR2(4) PRIMARY KEY NOT NULL,
                category_name VARCHAR2(50) NOT NULL
            )
            """
        )
        self.con.commit()

        self.cursor.execute(
            """
            CREATE TABLE link_book (
                link_book_id VARCHAR2(6) PRIMARY KEY NOT NULL,
                link_name VARCHAR2(50) NOT NULL,
                link_url VARCHAR2(5000) NOT NULL,
                link_category_id VARCHAR2(4),
                FOREIGN KEY (link_category_id) REFERENCES link_category(link_category_id)
            )
            """
        )
        self.con.commit()

        self.cursor.execute(
            """
            CREATE TABLE hotkey_details (
                hotkey_id VARCHAR2(5) PRIMARY KEY NOT NULL,
                hotkey VARCHAR2(200) NOT NULL,
                hotkey_desc VARCHAR2(500) NOT NULL,
                hotkey_destination VARCHAR2(500)
            )
            """
        )
        self.con.commit()

    def add_task(
            self,
            task_id,
            task_name,
            created_date,
            due_date,
            remind_date,
            remind_time,
            repeat,
            my_day,
            priority_lvl,
            status,
            important,
            list_id
    ):
        self.cursor.execute(
            f"""
            INSERT INTO task_details
            VALUES (
                '{task_id}',
                '{task_name}',
                '{created_date}',
                '{due_date}',
                '{remind_date}',
                '{remind_time}',
                '{repeat}',
                {my_day},
                '{priority_lvl}',
                {status},
                {important},
                '{list_id}'
            )
            """
        )
        self.con.commit()

    def update_task(
            self,
            task_id,
            task_name,
            created_date,
            due_date,
            remind_date,
            remind_time,
            repeat,
            my_day,
            priority_lvl,
            status,
            important,
            list_id
    ):
        self.cursor.execute(
            f"""
            UPDATE task_details
            SET
                task_name = '{task_name}',
                created_date = '{created_date}',
                due_date = '{due_date}',
                remind_date = '{remind_date}',
                remind_time = '{remind_time}',
                repeat = '{repeat}',
                my_day = {my_day},
                priority_lvl = '{priority_lvl}',
                status = {status},
                important = {important},
                list_id = '{list_id}'
            WHERE task_id = '{task_id}'
            """
        )
        self.con.commit()

    def update_task_status(
            self,
            task_id,
            status
    ):
        self.cursor.execute(
            f"""
            UPDATE task_details
            SET status = {status}
            WHERE task_id = '{task_id}'
            """
        )
        self.con.commit()

    def update_task_important(
            self,
            task_id,
            important
    ):
        self.cursor.execute(
            f"""
            UPDATE task_details
            SET important = {important}
            WHERE task_id = '{task_id}'
            """
        )
        self.con.commit()

    def remove_task(
            self,
            task_id,
            task_name
    ):
        self.cursor.execute(
            f"""
            DELETE FROM task_details
            WHERE task_id='{task_id}' AND task_name='{task_name}'
            """
        )
        self.con.commit()

    def add_list(
            self,
            list_id,
            list_name
    ):
        self.cursor.execute(
            f"""
            INSERT INTO list_details
            VALUES (
                '{list_id}',
                '{list_name}'
            )
            """
        )
        self.con.commit()

    def add_link_category(
            self,
            category_id,
            category_name
    ):
        self.cursor.execute(
            f"""
            INSERT INTO link_category
            VALUES(
                '{category_id}',
                '{category_name}'
            )
            """
        )
        self.con.commit()

    def update_link_category(
            self,
            category_id,
            category_name
    ):
        self.cursor.execute(
            f"""
            UPDATE link_category
            SET category_name = '{category_name}'
            WHERE category_id = '{category_id}'
            """
        )
        self.con.commit()

    def add_link_book(
            self,
            link_book_id,
            link_name,
            link_url,
            link_category_id
    ):
        self.cursor.execute(
            f"""
            INSERT INTO link_book
            VALUES(
                '{link_book_id}',
                '{link_name}',
                '{link_url}',
                '{link_category_id}'
            )
            """
        )
        self.con.commit()

    def update_link_book(
            self,
            link_book_id,
            link_name,
            link_url,
            link_category_id
    ):
        self.cursor.execute(
            f"""
            UPDATE link_book
            SET link_name = '{link_name}', link_url = '{link_url}', link_category_id = '{link_category_id}'
            WHERE link_book_id = '{link_book_id}'
            """
        )
        self.con.commit()

    def delete_link_category_row(
            self,
            link_category_id
    ):
        self.cursor.execute(
            f"""
            DELETE FROM link_category
            WHERE category_id = '{link_category_id}'
            """
        )
        self.con.commit()

    def delete_link_book_row(
            self,
            link_book_id
    ):
        self.cursor.execute(
            f"""
            DELETE FROM link_book
            WHERE link_book_id = '{link_book_id}'
            """
        )
        self.con.commit()

    def get_link_category(self):
        self.cursor.execute(
            """
            SELECT * FROM link_category
            """
        )
        return self.cursor.fetchall()

    def get_link_book(self):
        self.cursor.execute(
            """
            SELECT * FROM link_book
            """
        )
        return self.cursor.fetchall()

    def get_link_details_by_category(self, category_id):
        self.cursor.execute(
            f"""
            SELECT * FROM link_book
            WHERE link_category_id = '{category_id}'
            """
        )
        return self.cursor.fetchall()

    def add_hotkey(
            self,
            hotkey_id,
            hotkey,
            hotkey_desc,
            hotkey_Destination
    ):
        self.cursor.execute(
            f"""
            INSERT INTO hotkey_details
            VALUES(
                '{hotkey_id}',
                '{hotkey}',
                '{hotkey_desc}',
                '{hotkey_Destination}'
            )
            """
        )
        self.con.commit()

    def update_hotkey(
            self,
            hotkey_id,
            hotkey,
            hotkey_desc,
            hotkey_Destination
    ):
        self.cursor.execute(
            f"""
            UPDATE hotkey_details
            SET hotkey = '{hotkey}', hotkey_desc = '{hotkey_desc}', hotkey_destination = '{hotkey_Destination}'
            WHERE hotkey_id = '{hotkey_id}'
            """
        )
        self.con.commit()

    def delete_hotkey(
            self,
            hotkey_id
    ):
        self.cursor.execute(
            f"""
            DELETE FROM hotkey_details
            WHERE hotkey_id = '{hotkey_id}'
            """
        )
        self.con.commit()

    def delete_all_hotkeys(self):
        self.cursor.execute(
            f"""
            DELETE FROM hotkey_details
            """
        )
        self.con.commit()

    def get_hotkey_details(self):
        self.cursor.execute(
            """
            SELECT * FROM hotkey_details
            """
        )
        return self.cursor.fetchall()

    def get_task_details(self, is_sort=None):
        if is_sort is None:
            self.cursor.execute("SELECT * FROM task_details")
            return self.cursor.fetchall()
        elif is_sort:
            self.cursor.execute(
                """
                SELECT * FROM task_details
                ORDER BY created_date ASC;
                """
            )
            return self.cursor.fetchall()

    def get_myday_task_details(self, due_date, status):
        if due_date == None:
            self.cursor.execute(
                f"""
                SELECT * FROM task_details
                WHERE status = {status};
                """
            )
            # print(self.cursor.fetchall())
            return self.cursor.fetchall()
        elif status == None:
            self.cursor.execute(
                f"""
                SELECT * FROM task_details
                WHERE due_date = '{due_date}';
                """
            )
            # print(self.cursor.fetchall())
            return self.cursor.fetchall()
        else:
            self.cursor.execute(
                f"""
                SELECT * FROM task_details
                WHERE due_date = '{due_date}' AND status = {status};
                """
            )
            # print(self.cursor.fetchall())
            return self.cursor.fetchall()

    def custom_query_task_details(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_list_details(self):
        self.cursor.execute("SELECT * from list_details")
        return self.cursor.fetchall()

    def __del__(self):
        self.cursor.close()
        self.con.close()


if __name__ == '__main__':
    db = Database()
