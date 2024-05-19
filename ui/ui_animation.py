# -*- coding: utf-8 -*-
# @Project : SpriteSheetAnimation
# @Time    : 2024/5/19 9:31
# @Author  : jo-xin
# @File    : ui_animation.py

from ui import ui_mainwindow


class MainWindowAnimation(ui_mainwindow.UI_mainwindow):
    def __init__(self):
        super().__init__()

        self.frequency = 0
        self.duration = 0

        self.is_repeating = False

        MainWindowAnimation.initialize_connection(self)

    def initialize_connection(self):
        self.ui.pushButton_play.clicked.connect(self.play)
        self.ui.pushButton_stop.clicked.connect(self.stop)
        self.ui.pushButton_gif.clicked.connect(self.save_as_gif)
        self.ui.check_repeat.stateChanged.connect(self.set_repeat)
        self.ui.lineEdit_frequency.editingFinished.connect(self.frequency_changed)
        self.ui.lineEdit_duration.editingFinished.connect(self.duration_changed)

    def play(self) -> bool:
        test1 = self.is_positive_number(self.ui.lineEdit_duration.text())
        test2 = self.is_positive_number(self.ui.lineEdit_frequency.text())
        if test1 and test2:
            return True
        return False


    def stop(self):
        pass

    def set_repeat(self):
        pass

    def save_as_gif(self):
        pass

    def frequency_changed(self) -> bool:
        text = self.ui.lineEdit_frequency.text()
        if self.is_positive_number(text):
            self.frequency = float(text)
            self.duration = 1 / self.frequency
            self.ui.lineEdit_duration.setText(str(self.duration))
            return True
        return False

    def duration_changed(self) -> bool:
        text = self.ui.lineEdit_duration.text()
        if self.is_positive_number(text):
            self.duration = float(text)
            self.frequency = 1 / self.duration
            self.ui.lineEdit_frequency.setText(str(self.frequency))
            return True
        return False

    @staticmethod
    def is_positive_number(num_str: str):
        dot = num_str.count('.')
        if dot == 0:
            return num_str.isdigit()
        elif dot == 1:
            left, right = num_str.split('.')
            return left.isdigit() and right.isdigit()
        else:
            return False


