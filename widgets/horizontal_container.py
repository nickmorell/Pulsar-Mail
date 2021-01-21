from PyQt5.QtWidgets import *
from .mail_list import MailListWidget


class HorizontalContainer(QWidget):
    def __init__(self):
        super().__init__()
        self.__init_ui()

    def __init_ui(self):
        h_layout = QHBoxLayout()

        mail_list = MailListWidget()
        mail_list_2 = MailListWidget()
        mail_list_3 = MailListWidget()

        h_layout.setContentsMargins(0, 0, 0, 0)
        h_layout.setSpacing(0)
        h_layout.addWidget(mail_list)
        h_layout.addWidget(mail_list_2)
        h_layout.addWidget(mail_list_3,2)

        self.setLayout(h_layout)