import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from .mail_list import MailListWidget
from .horizontal_container import HorizontalContainer

class PulsarMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pulsar Mail")
        self.setWindowFlag(Qt.WindowContextHelpButtonHint)

        # card = MailCard()
        # mail_list_widget = MailListWidget()

        # self.setCentralWidget(mail_list_widget)
        # card.show()

        horizontal_content = HorizontalContainer()

        self.setCentralWidget(horizontal_content)

        self.show()
