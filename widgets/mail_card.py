from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class MailCard(QFrame):

    def __init__(self, sender='!Invalid Sender', receive_date='Just now', subject='!Invalid Subject', content='Unable to load content'):
        super(MailCard, self).__init__()
        self.init_ui(sender, receive_date, subject, content)

    def init_ui(self, sender='!Invalid Sender', receive_date='Just now', subject='!Invalid Subject', content='Unable to load content'):

        self.__create_sender_label(sender)
        self.__create_receive_date_label(receive_date)
        self.__create_subject_label(subject)
        self.__create_content_label(content)

        grid_layout = QGridLayout()

        grid_layout.addWidget(self.name_label, 0, 0, 1, 1)
        grid_layout.addWidget(self.date_label, 0, 1, 1, 1)
        grid_layout.addWidget(self.subject_label, 1, 0, 1, 2)
        grid_layout.addWidget(self.content_label, 2, 0, 1, 2)

        self.setLayout(grid_layout)

        self.setStyleSheet(f"background-color: white;"
                           "background-color: rgb(255, 255, 255);"
                           "border-radius: 7px;"
                           )

    def __create_sender_label(self, sender='!Invalid Sender'):
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setPixelSize(14)

        self.name_label = QLabel(sender)
        self.name_label.setFont(font)
        self.name_label.setStyleSheet(u"margin-top:1px;")

    def __create_receive_date_label(self, receive_date='Just now'):
        font = QFont()
        font.setPixelSize(10)

        self.date_label = QLabel(receive_date)
        self.date_label.setStyleSheet(u"color: rgb(188, 189, 191)")
        self.date_label.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.date_label.setFont(font)

    def __create_subject_label(self, subject='!Invalid Subject'):
        font = QFont()
        font.setPixelSize(12)

        self.subject_label = QLabel(subject)
        self.subject_label.setStyleSheet(u"color: rgb(108, 108, 108)")
        self.subject_label.setFont(font)

    def __create_content_label(self, content='Unable to load content'):
        font = QFont()
        font.setPixelSize(12)

        self.content_label = QLabel(content)
        self.content_label.setStyleSheet(u"color: rgb(188, 189, 191)")
        self.content_label.setWordWrap(True)
        self.content_label.setFont(font)