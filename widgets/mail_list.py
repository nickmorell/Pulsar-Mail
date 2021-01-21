from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from .mail_card import MailCard


class MailListWidget(QScrollArea):
    def __init__(self):
        super().__init__()

        self.vbox = QVBoxLayout()
        self.widget = QWidget()

        self.init_ui()

    def init_ui(self):
        for i in range(1,3):
            card = MailCard()
            self.vbox.addWidget(card)
            card.setAutoFillBackground(True)
            # card.setStyleSheet(f"background-color: white;")
            card.setStyleSheet(f"background-color: white;"
                               "background-color: rgb(255, 255, 255);"
                               "border-radius: 7px;"
                               )

        self.widget.setLayout(self.vbox)
        # self.widget.setMinimumWidth(325)

        # Scroll Area Properties
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)


        self.setMinimumHeight(100)
        self.setMaximumHeight(125)
        self.setMinimumWidth(300)
        self.setMaximumWidth(300)
        self.setWidget(self.widget)