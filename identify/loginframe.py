from PyQt5.QtWidgets import QDialog,QMessageBox
from identify.loginui import Ui_Dialog
from identify.idenframe import IdenDialog
class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def login(self):
        # 获取输入的用户名和密码
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        # 预设的正确用户名和密码
        correct_username = "0211123400"
        correct_password = "xy040728"

        # 检查输入的用户名和密码是否正确
        if username == correct_username and password == correct_password:
            # 登录成功，执行golo方法
            self.golo()
        else:
            # 登录失败，显示错误消息
            QMessageBox.warning(self, "Login Failed", "Incorrect username or password!")
    def golo(self):
        self.monitorframe = IdenDialog()
        self.monitorframe.show()
        self.close()

