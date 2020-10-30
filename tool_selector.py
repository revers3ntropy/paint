# ================================================================================================
# |------------------------------------={ Project Name }=----------------------------------------|
# ================================================================================================
#
#                                   Programmers : Joseph Coppin
#
#                                     File Name : button.py
#
#                                       Created : Month 00, 2020
#
# ------------------------------------------------------------------------------------------------
#
#   Imports:
import pygame as py

from button import Buttons
import renderer
#
# ------------------------------------------------------------------------------------------------
#
#                                       What the file does.
#
# ------------------------------------------------------------------------------------------------
#
# ================================================================================================


class ToolSelectManager:
    def __init__(self):
        self.select = False

        self.pen = 0
        self.bucket = 1

        tools = {
            self.pen: py.image.load('pen.gif'),
            self.bucket: py.image.load('bucket.gif')
        }

        self.current_tool = self.pen

        self.buttons = []
        button_size = 15
        current_hitbox = [
            renderer.screen_x / 2 - (len(tools) * button_size),
            button_size + 50,
            button_size,
            button_size
        ]

        for tool in range(len(tools)):
            self.buttons.append(ToolSelector(tool, tuple(current_hitbox), tools[tool]))
            current_hitbox[0] += button_size * 2

    def run(self):
        keys = py.key.get_pressed()
        if keys[py.K_p]:
            self.current_tool = self.pen
        elif keys[py.K_b]:
            self.current_tool = self.bucket
        self.select = False

        for button in self.buttons:
            if button.run(self.current_tool):
                self.current_tool = button.tool

            if button.moused:
                self.select = True


class ToolSelector(Buttons):
    def __init__(self, tool, hitbox, image):
        super().__init__(hitbox)
        self.tool = tool
        self.radius = (self.hitbox[2] + self.hitbox[3]) / 2
        self.image = image

    def run(self, current_tool):
        click_box = (self.hitbox[0] - self.radius * 3 + 40, self.hitbox[1] - self.radius * 3 + 40, self.hitbox[2] + self.radius, self.hitbox[3] + self.radius)
        self.check_mouse(click_box)

        if self.moused:
            if current_tool == self.tool:
                colour = (50, 50, 50)
            else:
                colour = (100, 100, 100)
        else:
            if current_tool == self.tool:
                colour = (150, 150, 150)
            else:
                colour = (200, 200, 200)

        py.draw.circle(renderer.screen, colour, (self.hitbox[0], self.hitbox[1]), self.radius)

        renderer.screen.blit(self.image, (self.hitbox[0] - 10, self.hitbox[1] - 10))

        if self.check_clicked():
            return True

