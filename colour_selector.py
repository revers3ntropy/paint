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


class ColourSelectManager:
    def __init__(self):
        self.select = False
        self.current_colour = (0, 0, 0)

        colours = [
            (0, 0, 0),
            (128, 128, 128),
            (255, 255, 255),
            (255, 0, 0),
            (0, 255, 0),
            (0, 0, 255)
        ]

        self.buttons = []

        button_size = 15
        current_hitbox = [
            renderer.screen_x / 2 - (len(colours) * button_size),
            button_size + 10,
            button_size,
            button_size
        ]

        for colour in colours:
            self.buttons.append(ColourSelector(colour, tuple(current_hitbox)))
            current_hitbox[0] += button_size * 2

    def run(self):
        self.select = False
        for button in self.buttons:
            if button.run():
                self.current_colour = button.colour

            if button.moused:
                self.select = True


class ColourSelector(Buttons):
    def __init__(self, colour, hitbox):
        super().__init__(hitbox)
        self.colour = colour
        self.radius = (self.hitbox[2] + self.hitbox[3]) / 2
        self.select_radius = self.radius + 1

    def run(self):
        click_box = (self.hitbox[0] - self.radius, self.hitbox[1] - self.radius, self.hitbox[2] + self.radius, self.hitbox[3] + self.radius)
        self.check_mouse(click_box)
        if self.moused:
            py.draw.circle(renderer.screen, (0, 0, 0), (self.hitbox[0], self.hitbox[1]), self.select_radius)
            moused = True
        else:
            moused = False

        py.draw.circle(renderer.screen, self.colour, (self.hitbox[0], self.hitbox[1]), self.radius)

        if self.check_clicked():
            return True

        return moused
