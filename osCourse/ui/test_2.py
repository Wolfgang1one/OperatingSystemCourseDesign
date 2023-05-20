import sys

from PyQt5 import QtWidgets, uic

from menu import Ui_menu
from P import Ui_P
from J import Ui_J

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QStackedWidget


class set_Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi('./menu.ui')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # myshow = set_Menu()
    # myshow.ui.show()
    myShow = QWidget()
    myShow.ui = uic.loadUi("./menu.ui")
    myShow.ui.pushButton
    myShow.ui.show()
    sys.exit(app.exec_())
