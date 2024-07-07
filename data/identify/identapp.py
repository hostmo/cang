from PyQt5.QtWidgets import QApplication
from identify.mainframe import MainDialog
import sys
class IdentApp(QApplication):
    def __init__(self):
        super(IdentApp,self).__init__(sys.argv)
        self.dialog=MainDialog()
        self.dialog.show()
