# -*- coding: utf-8 -*-
# @Project : SpriteSheetAnimation
# @Time    : 2024/5/18 22:54
# @Author  : jo-xin
# @File    : ui_spriteSheet.py

from ui import ui_mainwindow
from PyQt6.QtGui import QDragEnterEvent, QDragMoveEvent, QDropEvent, QPixmap
from PyQt6.QtCore import Qt


class MainWindowSheet(ui_mainwindow.UI_mainwindow):
    def __init__(self):
        super().__init__()

        self.sheet_url = ""

        self.sheet_size = (0, 0)
        self.frame_size = (0, 0)
        self.grid_size = (0, 0)
        self.stop_after = (0, 0)
        self.is_row_major_order = True

        MainWindowSheet.initialize_connection(self)

    def initialize_connection(self):
        self.ui.pushButton_guess.clicked.connect(self.guess)
        self.ui.pushButton_split.clicked.connect(self.split)

    def guess(self) -> bool:
        if self.check_digit():
            self.read_input()
            return True
        return False

    def split(self) -> bool:
        if self.check_digit():
            self.read_input()
            if self.check_validity():
                return True
        return False

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event: QDragMoveEvent):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasImage:
            event.setDropAction(Qt.DropAction.CopyAction)
            event.accept()
            self.sheet_url = event.mimeData().urls()[0].toLocalFile()
            self.accept_drop()

    def accept_drop(self):
        pass

    def show_sheet(self, img: QPixmap):
        self.ui.label_sheet.setPixmap(img.scaled(self.ui.label_sheet.width(),
                                                 self.ui.label_sheet.height(),
                                                 Qt.AspectRatioMode.KeepAspectRatio))
        self.ui.label_sheetInfo.setText(f"Width: {img.width()}  Height: {img.height()}")

    def check_digit(self) -> bool:
        ret = True
        lines = (self.ui.lineEdit_columns,
                 self.ui.lineEdit_rows,
                 self.ui.lineEdit_frameW,
                 self.ui.lineEdit_frameH,
                 self.ui.lineEdit_stopColumn,
                 self.ui.lineEdit_stopRow)

        for line in lines:
            if not self.check_line_digit(line):
                ret = False
        return ret

    def read_input(self):
        inputs = []
        lines = (self.ui.lineEdit_columns,
                 self.ui.lineEdit_rows,
                 self.ui.lineEdit_frameW,
                 self.ui.lineEdit_frameH,
                 self.ui.lineEdit_stopColumn,
                 self.ui.lineEdit_stopRow)
        for line in lines:
            if line.text() == "":
                inputs.append(0)
            else:
                inputs.append(int(line.text()))

        self.grid_size = (inputs[0], inputs[1])
        self.frame_size = (inputs[2], inputs[3])
        self.stop_after = (inputs[4], inputs[5])

        self.is_row_major_order = self.ui.check_rowMajor.isChecked()

    def write_inputs(self):
        lines = (self.ui.lineEdit_columns,
                 self.ui.lineEdit_rows,
                 self.ui.lineEdit_frameW,
                 self.ui.lineEdit_frameH,
                 self.ui.lineEdit_stopColumn,
                 self.ui.lineEdit_stopRow)
        values = (self.grid_size[0],
                  self.grid_size[1],
                  self.frame_size[0],
                  self.frame_size[1],
                  self.stop_after[0],
                  self.stop_after[1])
        for i in range(5):
            if values[i] == 0:
                lines[i].setText("")
            else:
                lines[i].setText(str(values[i]))

    def check_validity(self) -> bool:
        ret = True

        if self.frame_size[0] == 0 and self.grid_size[0]:
            self.prompt_red(self.ui.lineEdit_frameW)
            self.prompt_red(self.ui.lineEdit_columns)
            self.ui.statusbar.showMessage("please finish at least one for each dimension!")
            ret = False
        if self.frame_size[0] * self.grid_size[0] > self.sheet_size[0]:
            self.prompt_red(self.ui.lineEdit_frameW)
            self.prompt_red(self.ui.lineEdit_columns)
            self.ui.statusbar.showMessage("sheet size is smaller than calculated!")
            ret = False

        if self.frame_size[1] == 0 and self.grid_size[1]:
            self.prompt_red(self.ui.lineEdit_frameH)
            self.prompt_red(self.ui.lineEdit_rows)
            self.ui.statusbar.showMessage("please finish at least one for each dimension!")
            ret = False
        if self.frame_size[1] * self.grid_size[1] > self.sheet_size[1]:
            self.prompt_red(self.ui.lineEdit_frameH)
            self.prompt_red(self.ui.lineEdit_rows)
            self.ui.statusbar.showMessage("sheet size is smaller than calculated!")
            ret = False

        return ret
