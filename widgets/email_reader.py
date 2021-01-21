from PyQt5.QtWidgets import *
from PyQt5 import QtWebEngineWidgets

class EmailReader(QWidget):
    def __init__(self):
        super().__init__()
        self.__init_ui()

    def __init_ui(self):
        grid_layout = QVBoxLayout()

        self.html = QtWebEngineWidgets.QWebEngineView()
        # self.html.setReadOnly(True)
        self.html.setHtml('<!DOCTYPE HTML><HTML><head><style>h1{color:red}</style></head><body><h1>Hello World</h1><p>Will This display</p></body></HTML>')
        grid_layout.addWidget(self.html)

        # self.setGeometry(9000, 90000, 90000, 90000)
        grid_layout.setSpacing(0)
        grid_layout.setContentsMargins(0,0,0,0)

        self.setLayout(grid_layout)
