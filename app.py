from tkinter import *
from database import Database
from PyQt5.QtWidgets import QApplication, QLabel
from email_handler.imap_handler import IMAPHandler
import sys
from widgets.splash_screen import SplashScreen
from widgets.main_window import PulsarMain

class MainApplication(QApplication):
    def __init__(self):
        app = SplashScreen()

        app.show()
        sys.exit(app.exec_())


def createTopBar(TopLevel):
    frame = Frame(master=TopLevel, height=50, bg="white")

    return frame


def createAccountFrame(TopLevel):
    frame = Frame(master=TopLevel, width=400, bg="white")

    composeButton = Button(master=frame, text="Compose", bg="#e54065")
    composeButton.pack()
    return frame


# def createSideBar(window):
#     canvas=Canvas(window,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,500,500))
#     vertical_scrollbar = Scrollbar(canvas, orient=tk.VERTICAL)
#     vertical_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
#     vertical_scrollbar.config(command=canvas.yview)
#     canvas.config(width=300,height=300)
#     canvas.config(yscrollcommand=vertical_scrollbar.set)
#     return canvas

def createMessageWidget(window):
    return Text(master=window, width=50, height=50, bg="white")


def start_pulsar():
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()

    sys.exit(app.exec_())

    # #Main Window
    # Toplevel = Tk()
    # Toplevel.title("Pulsar")
    # Toplevel.minsize(500,500)
    #
    # #TopBar
    # topBar = createTopBar(Toplevel)
    # topBar.grid(row=0)
    #
    # # Left Side Bar
    # accountFrame = createAccountFrame(Toplevel)
    # accountFrame.grid(row=1, column=0, columnspan=6)
    #
    # # Middle Frame (Mail List)
    #
    # # Right Side Frame (Detailed Message)
    # messageWidget = createMessageWidget(Toplevel)
    # messageWidget.grid(row=1, column=7, columnspan=2)
    #
    # Toplevel.mainloop()


if __name__ == "__main__":
    pulsarDb = Database()
    # accounts = pulsarDb.select(sql='SELECT * FROM account A WHERE A.disabled = 0')
    #
    # for account in accounts:
    #     account_connection = pulsarDb.select('SELECT * FROM account_connection AC WHERE AC.accountId={}'.format(account[0]))[0]
    #
    #     if account_connection[1] == 'IMAP':
    #         handler = IMAPHandler(account_connection[2], account[1], account[2])
    #         mailboxes = handler.refresh_mailboxes()
    #         messages = handler.refresh_mail(mailboxes)
    #
    #         for message in messages:
    #             for mailbox_name, email_content in message.items():
    #                 print('Mailbox: {} - Length: {}'.format(mailbox_name, len(email_content)))
    #
    # pulsarDb.close_connection()
    #
    # start_pulsar()

    app = QApplication(sys.argv)
    splash_screen = SplashScreen()
    splash_screen.show()
    app.processEvents()
    isLoaded = splash_screen.begin_loading(pulsarDb)
    if isLoaded:
        splash_screen.destroy()
        pulsarApp = PulsarMain()
        pulsarApp.show()
    sys.exit(app.exec_())

