import win32com.client
#other libraries to be used in this script
import os
from datetime import datetime, timedelta

class OutlookHandler:
    def __init__(self):
        super().__init__()

    def get_mail(self, username, password):
        outlook = win32com.client.Dispatch('outlook.application')
        mapi = outlook.GetNamespace("MAPI")


