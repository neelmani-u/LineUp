# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(546, 509)
        self.verticalLayout = QVBoxLayout(MainPages)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.pages.addWidget(self.dashboard_page)
        self.task_manager_page = QWidget()
        self.task_manager_page.setObjectName(u"task_manager_page")
        self.pages.addWidget(self.task_manager_page)
        self.task_manager_page_layout = QVBoxLayout(self.task_manager_page)
        self.task_manager_page_layout.setObjectName(u"task_manager_page_layout")
        self.link_book_page = QWidget()
        self.link_book_page.setObjectName(u"link_book_page")
        self.pages.addWidget(self.link_book_page)
        self.link_book_page_layout = QVBoxLayout(self.link_book_page)
        self.link_book_page_layout.setObjectName(u"link_manager_page_layout")
        self.hotkeys_page = QWidget()
        self.hotkeys_page.setObjectName(u"hotkeys_page")
        self.pages.addWidget(self.hotkeys_page)
        self.hotkeys_page_layout = QVBoxLayout(self.hotkeys_page)
        self.hotkeys_page_layout.setObjectName(u"hotkeys_manager_page_layout")
        self.automata_page = QWidget()
        self.automata_page.setObjectName(u"automata_page")
        self.pages.addWidget(self.automata_page)
        self.powerboard_page = QWidget()
        self.powerboard_page.setObjectName(u"powerboard_page")
        self.pages.addWidget(self.powerboard_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.pages.addWidget(self.settings_page)

        self.verticalLayout.addWidget(self.pages)

        self.retranslateUi(MainPages)

        QMetaObject.connectSlotsByName(MainPages)

    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
    # retranslateUi
