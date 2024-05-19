# -*- coding: utf-8 -*-
# @Project : SpriteSheetAnimation
# @Time    : 2024/5/19 12:10
# @Author  : jo-xin
# @File    : main.py


import sys
from PyQt6.QtWidgets import QApplication
import mainwindow


class App(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.window = mainwindow.MainWindow()

    def exec(self):
        self.window.show()
        super().exec()


if __name__ == '__main__':
    app = App(sys.argv)
    ret = app.exec()
    sys.exit(ret)
