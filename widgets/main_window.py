from PyQt5.Qt import QDesktopServices
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from .horizontal_container import HorizontalContainer


class PulsarMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pulsar Mail")
        self.setWindowFlag(Qt.WindowContextHelpButtonHint)  # Remove ? button in title bar

        self.setWindowState(Qt.WindowMaximized)

        # Menu Bar Creation
        self.__create_menu_bar()

        # Main 3 Columned Layout Creation
        central_widget = HorizontalContainer()
        # central_widget.setStyleSheet(u'background-color:red;')
        central_widget.setGeometry(0, 0, 16777215, 16777215)
        self.setCentralWidget(central_widget)

        self.show()

    def __create_menu_bar(self):
        menu_bar = QMenuBar()
        menu_bar.setNativeMenuBar(False)

        # # File Menu
        file_menu = menu_bar.addMenu('&File')

        exit_action = QAction('&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit Application')
        exit_action.triggered.connect(qApp.quit)
        file_menu.addAction(exit_action)

        # # Edit Menu
        edit_menu = menu_bar.addMenu('&Edit')

        # Help Menu
        help_menu = menu_bar.addMenu('&Help')

        source_code_action = QAction('&Source Code', self)
        source_code_action.setStatusTip('View Pulsar Mail source code on Github')
        source_code_action.triggered.connect(self.open_source_code_link)

        check_update_action = QAction('&Check for updates', self)
        check_update_action.setStatusTip('Check for updates')

        about_action = QAction('&About', self)
        about_action.setStatusTip('Learn about Pulsar Mail')

        help_menu.addAction(source_code_action)
        help_menu.addAction(check_update_action)
        help_menu.addAction(about_action)

        self.setMenuBar(menu_bar)

    @pyqtSlot()
    def open_source_code_link(self):
        QDesktopServices.openUrl(QUrl("https://github.com/nickmorell/Pulsar-Mail"))
