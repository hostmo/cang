from PyQt5.QtWidgets import QDialog,QMessageBox
from identify.loginui import Ui_Dialog
from identify.idenframe import IdenDialog
class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def login(self):
        # ��ȡ������û���������
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        # Ԥ�����ȷ�û���������
        correct_username = "0211123400"
        correct_password = "xy040728"

        # ���������û����������Ƿ���ȷ
        if username == correct_username and password == correct_password:
            # ��¼�ɹ���ִ��golo����
            self.golo()
        else:
            # ��¼ʧ�ܣ���ʾ������Ϣ
            QMessageBox.warning(self, "Login Failed", "Incorrect username or password!")
    def golo(self):
        self.monitorframe = IdenDialog()
        self.monitorframe.show()
        self.close()

