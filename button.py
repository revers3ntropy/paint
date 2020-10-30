# ================================================================================================
# |------------------------------------={ Project Name }=----------------------------------------|
# ================================================================================================
#
#                                   Programmers : Joseph Coppin
#
#                                     File Name : file_name.py
#
#                                       Created : Month 00, 2020
#
# ------------------------------------------------------------------------------------------------
#
#   Imports:
import curser
#
# ------------------------------------------------------------------------------------------------
#
#                                       What the file does.
#
# ------------------------------------------------------------------------------------------------
#
#
# ================================================================================================


class Buttons:
    def __init__(self, hitbox):
        self.hitbox = hitbox
        self.moused = False

    def check_mouse(self, hit_box):
        if curser.check_mouse_collision(hit_box):
            self.moused = True
        else:
            self.moused = False

    def check_clicked(self):
        if self.moused and curser.check_new_click():
            return True
        return False
