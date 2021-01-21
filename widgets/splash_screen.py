import time

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class SplashScreen(QSplashScreen):

    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(640, 480))
        self.setWindowTitle("Hello world - pythonprogramminglanguage.com")

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.__center_screen()

        grid_layout = QGridLayout(self)
        self.setLayout(grid_layout)

        self.loading_label = QLabel("Loading...", self)
        self.loading_label.setAlignment(Qt.AlignCenter)
        grid_layout.addWidget(self.loading_label, 0, 0)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(30, 40, 200, 25)
        self.progress_bar.setAlignment(Qt.AlignCenter)
        self.progress_bar.setRange(0, 5)
        grid_layout.addWidget(self.progress_bar, 1, 0)

    def begin_loading(self, database):
        self.__create_databases(database)
        self.__load_accounts(database)
        return True

    def __center_screen(self):
        qt_rectangle = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        qt_rectangle.moveCenter(center_point)
        self.move(qt_rectangle.topLeft())

    def __create_databases(self, database):
        self.loading_label.setText('Checking Database Integrity...')
        database.run(
            "CREATE TABLE IF NOT EXISTS account(accountId INTEGER constraint account_pk primary key autoincrement, email varchar(255), password varchar(255), disabled INTEGER default 0 not null);")
        database.run("CREATE UNIQUE INDEX account_email_uindex on account (email);")
        database.run(
            "CREATE TABLE IF NOT EXISTS account_connection (accountConnectionId INTEGER constraint account_connection_pk primary key autoincrement, protocol varchar(10) not null, connection_url varchar(255) not null, accountId INTEGER, constraint account_connection_account__accountId_fk foreign key (accountId, accountId) references account ('accountId', accountId) on update cascade on delete cascade);")
        self.progress_bar.setValue(1)

        return True

    def __load_accounts(self, database):
        self.loading_label.setText('Loading Accounts')
        time.sleep(2)
        accounts = database.select(sql='SELECT * FROM account A WHERE A.disabled = 0')
        self.progress_bar.setValue(2)