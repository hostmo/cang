from PyQt5.QtWidgets import QDialog
from identify.miui import Ui_Dialog
import sys
from PyQt5.QtCore import QTimer
class InformDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showtxt)
        self.timer.start(1000)


    def showtxt(self):
        try:
            with open('data/information.txt', 'r') as file:
                text = file.read()
                self.ui.label.setText(text)
        except Exception as e:
            print(f"An error occurred: {e}")
