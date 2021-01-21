from PyQt5.Qt import *
from .mail_card import MailCard


class MailListWidget(QScrollArea):
    def __init__(self):
        super().__init__()

        self.vbox = QVBoxLayout()
        self.widget = QWidget()

        self.init_ui()

    def init_ui(self):
        self.__set_vbox_settings()
        self.__set_scroll_area_settings()

        for i in range(1, 200):
            card = MailCard()
            self.vbox.addWidget(card)
            card.setAutoFillBackground(True)
            card.setStyleSheet(f"background-color: white;"
                               "background-color: rgb(255, 255, 255);"
                               "border-radius: 7px;"
                               )
            card.setMaximumHeight(100)
            card.setMinimumHeight(100)

        self.widget.setLayout(self.vbox)

    def __set_scroll_area_settings(self):
        # Scroll Area Properties
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)

        self.setMinimumWidth(300)
        self.setWidget(self.widget)
        self.setContentsMargins(5, 5, 5, 5)

    def __set_vbox_settings(self):
        self.vbox.setContentsMargins(5, 5, 5, 5)
        self.vbox.setSpacing(5)
        self.vbox.setStretch(0, 0)
