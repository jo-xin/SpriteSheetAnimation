# -*- coding: utf-8 -*-
# @Project : SpriteSheetAnimation
# @Time    : 2024/5/18 19:22
# @Author  : jo-xin
# @File    : animation.py

from PIL import ImageQt
from PIL.Image import Image
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class AnimationShower:
    def __init__(self, label: QLabel):
        """
        class that show the animation
        :param label: label to show the animation
        """
        self.label = label
        self.timer = QTimer()
        self.frames: list[QPixmap] = []

        self.duration = 1000
        self.current_frame = 0
        self.frames_length = len(self.frames)

        self.do_repeat = False

        self.timer.timeout.connect(self.draw_frame)

    def read_frames(self, images: list[Image]):
        """
        store the frames as QPixmap
        :param images: frames in Image
        :return:
        """
        self.frames = []
        for image in images:
            self.frames.append(ImageQt.toqpixmap(image))
        self.frames_length = len(self.frames)

    def draw_frame(self):
        """
        show the next frame in the label
        :return:
        """
        self.label.setPixmap(self.frames[self.current_frame].scaled(self.label.width(),
                                                                    self.label.height(),
                                                                    Qt.AspectRatioMode.KeepAspectRatio))
        self.current_frame = (self.current_frame + 1) % self.frames_length
        if self.current_frame == 0 and not self.do_repeat:
            self.timer.stop()

    def start(self):
        """
        start animation
        :return:
        """
        self.current_frame = 0
        self.timer.start(int(self.duration * 1000))

    def stop(self):
        """
        stop animation
        :return:
        """
        self.timer.stop()
        self.current_frame = 0

    def is_running(self) -> bool:
        """
        if the timer is running
        :return: isRunning
        """
        return self.timer.isActive()


