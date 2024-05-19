# -*- coding: utf-8 -*-
# @Project : SpriteSheetAnimation
# @Time    : 2024/5/19 9:32
# @Author  : jo-xin
# @File    : mainwindow.py

from ui import ui_frames, ui_animation, ui_spriteSheet
import image_process, animation


class MainWindow(ui_spriteSheet.MainWindowSheet, ui_frames.MainWindowFrames, ui_animation.MainWindowAnimation):
    def __init__(self):
        super().__init__()

        self.image_process = image_process.ImageProcess()
        self.animation = animation.AnimationShower(self.ui.label_animation)

    def accept_drop(self):
        self.image_process.read_sprite_sheet(self.sheet_url)
        self.sheet_size = self.image_process.spriteSheet.size
        self.show_sheet(self.image_process.show_sheet())

    def guess(self):
        if super().guess():
            self.image_process.splitTool.guess_splitting()
            self.frame_size = self.image_process.splitTool.frame_size
            self.grid_size = self.image_process.splitTool.grid_size
            x, y = self.image_process.splitTool.stop_after
            self.stop_after = (x + 1, y + 1)
            self.is_row_major_order = self.image_process.splitTool.is_row_major_order
            self.write_inputs()

    def split(self):
        if super().split():
            self.image_process.splitTool.frame_size = self.frame_size
            self.image_process.splitTool.grid_size = self.grid_size
            x, y = self.stop_after
            self.image_process.splitTool.stop_after = (x - 1, y - 1)
            self.image_process.splitTool.is_row_major_order = self.is_row_major_order
            self.image_process.split()
            self.animation.read_frames(self.image_process.frames)

    def play(self):
        if super().play():
            self.animation.duration = self.duration
            self.animation.start()

    def stop(self):
        self.animation.stop()

    def set_repeat(self):
        self.animation.do_repeat = self.ui.check_repeat.isChecked()

    def save_as_gif(self):
        self.image_process.img_to_gif(self.duration)








