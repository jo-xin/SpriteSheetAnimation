# -*- coding: utf-8 -*-
# @Project : SpriteSheetAnimation
# @Time    : 2024/5/19 9:39
# @Author  : jo-xin
# @File    : ui_mainwindow.py

from PyQt6.QtWidgets import QMainWindow, QLineEdit
from PyQt6.QtGui import QIcon
from ui.ui_file import mianwindow


class UI_mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = mianwindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.setup_icon()


    def setup_icon(self):
        self.ui.pushButton_guess.setIcon(QIcon("./assets/icons/auto.png"))
        self.ui.pushButton_play.setIcon(QIcon("./assets/icons/play.png"))
        self.ui.pushButton_stop.setIcon(QIcon("./assets/icons/stop.png"))
        self.ui.check_repeat.setIcon(QIcon("./assets/icons/repeat.png"))
        self.setWindowIcon(QIcon("./assets/icons/crop.png"))

    @staticmethod
    def prompt_red(line: QLineEdit):
        line.setStyleSheet("border: 2px outset red")

    @staticmethod
    def prompt_none(line: QLineEdit):
        line.setStyleSheet("")

    def check_line_digit(self, line: QLineEdit) -> bool:
        ret = True
        if not (line.text().isdigit() or line.text() == ""):
            self.prompt_red(line)
            self.ui.statusbar.showMessage("inputs should be all digits!", 5000)
            ret = False
        else:
            self.prompt_none(line)

        return ret



