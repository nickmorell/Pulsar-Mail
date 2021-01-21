from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from .mail_list import MailListWidget
from .email_reader import EmailReader


class HorizontalContainer(QWidget):
    def __init__(self):
        super().__init__()
        self.__init_ui()

    def __init_ui(self):
        # h_layout = QHBoxLayout()
        grid_layout = QGridLayout()

        mail_list = MailListWidget()
        mail_list.setMaximumWidth(300)
        mail_list_2 = MailListWidget()
        mail_list_2.setMaximumWidth(300)
        # mail_list_3 = MailListWidget()
        email_reader = EmailReader()

        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setSpacing(0)

        # addWidget (self, QWidget, row, column, rowSpan, columnSpan, Qt.Alignment alignment = 0)
        # grid_layout.addWidget(mail_list, 0, 0, 1, 1)
        grid_layout.addWidget(mail_list, 0, 0, 0, 1)
        grid_layout.addWidget(mail_list_2, 0, 1, 0, 1)
        grid_layout.addWidget(email_reader, 0, 2, 0, 2)

        self.setLayout(grid_layout)
