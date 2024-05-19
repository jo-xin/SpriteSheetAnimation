# -*- coding: utf-8 -*-
# @Project : SpriteSheetAnimation
# @Time    : 2024/5/18 14:59
# @Author  : jo-xin
# @File    : image_process.py

import PIL.Image as Image
from PIL import ImageQt
from PyQt6.QtGui import QPixmap
import math
import os.path


class SplitTool:
    def __init__(self):
        """
        do all the jobs with splitting
        """
        self.spriteSheet: Image.Image | None = None

        self.sheet_size: tuple[int, int] = (0, 0)
        self.frame_size: tuple[int, int] = (0, 0)
        self.grid_size: tuple[int, int] = (0, 0)

        self.is_row_major_order: bool = True

        self.stop_after: tuple[int, int] = (0, 0)

    def read_sheet(self, sheet: Image.Image):
        """
        read the spriteSheet
        :param sheet: Image object
        :return:
        """
        self.spriteSheet = sheet
        self.sheet_size = sheet.size

    def crop(self, pair: tuple[int, int]) -> Image.Image:
        """
        crop the indicated frame from the sprite sheet
        :param pair: coordinate in the grid
        :return: cropped frame image
        """
        x0 = self.frame_size[0] * pair[0]
        y0 = self.frame_size[1] * pair[1]
        x1 = x0 + self.frame_size[0]
        y1 = y0 + self.frame_size[1]
        return self.spriteSheet.crop((x0, y0, x1, y1))

    def split(self) -> list[Image.Image]:
        """
        split the frames and return
        :return: frames
        """
        images = []
        for x, y in self.split_coordinates():
            images.append(self.crop((x, y)))
        return images

    def split_coordinates(self):
        """
        a generator that gives the grid coordinates in the correct order
        :return: grid coordinate
        """
        stop_after = self.stop_after
        if stop_after == (0, 0):
            stop_after = self.grid_size

        if not self.is_row_major_order:
            for x in range(self.grid_size[0]):
                for y in range(self.grid_size[1]):
                    yield x, y
                    if (x, y) == stop_after:
                        return
        else:
            for y in range(self.grid_size[1]):
                for x in range(self.grid_size[0]):
                    yield x, y
                    if (x, y) == stop_after:
                        return

    def guess_splitting(self):
        """
        regard the frame as a square, and gcd of sheet size as length of sides
        :return:
        """
        gcd = math.gcd(self.sheet_size[0], self.sheet_size[1])
        self.frame_size = (gcd, gcd)
        self.grid_size = (self.sheet_size[0] // self.frame_size[0],
                          self.sheet_size[1] // self.frame_size[1])

        self.guess_stop_after()

    def guess_stop_after(self):
        """
        guess where to stop
        :return:
        """
        stop_after = (0, 0)
        for x, y in self.split_coordinates():
            if self.guess_null_frame(self.crop((x, y))):
                break
            stop_after = (x, y)
        self.stop_after = stop_after

    @staticmethod
    def guess_null_frame(frame: Image.Image):
        """
        test if the frame is null, i.e. all transparent
        :return: if it's all transparent
        """
        for x in range(frame.size[0]):
            for y in range(frame.size[1]):
                if frame.getpixel((x, y))[3] != 0:
                    return False
        return True


class ImageProcess:
    def __init__(self):
        """
        class that does all the jobs with image
        """
        self.is_sheet_read: bool = False
        self.is_sheet_split: bool = False

        self.sheet_path: str = ""
        self.spriteSheet: Image.Image | None = None
        self.frames: list[Image.Image] | None = None

        self.splitTool = SplitTool()

    def read_sprite_sheet(self, file_path: str):
        """
        read the sprite sheet from the path
        :param file_path: file path
        :return:
        """
        self.sheet_path = file_path
        self.spriteSheet = Image.open(file_path).convert('RGBA')
        self.splitTool.read_sheet(self.spriteSheet)

        self.is_sheet_read = True
        self.is_sheet_split = False

    def show_sheet(self) -> QPixmap:
        return ImageQt.toqpixmap(self.spriteSheet)

    def split(self):
        """
        split the sprite sheet into frames
        :return:
        """
        self.frames = self.splitTool.split()

        self.is_sheet_split = True

    def img_to_gif(self, duration: float):
        """
        derive a gif from images with indicated fps
        :param duration: duration per frame
        :return:
        """
        save_name = os.path.splitext(os.path.basename(self.sheet_path))[0] + ".gif"
        self.frames[0].save(save_name,
                            save_all=True,
                            append_images=self.frames,
                            duration=duration,
                            transparency=0,
                            disposal=2)











