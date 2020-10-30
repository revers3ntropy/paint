# ================================================================================================
# |                                       Joseph Coppin                                         |
# ================================================================================================
#
#                                  Project Name : Computer Science GSCE Coursework
#
#                                     File Name : cursor.py
#
#                                       Created : July 27, 2020
#
#                                   Last Update : October 21, 2020
#
# ------------------------------------------------------------------------------------------------
#
#                            Controls mouse collisions and clicks.
#
# ------------------------------------------------------------------------------------------------
#
# Imports:
import pygame as py
#
# ------------------------------------------------------------------------------------------------
#
#	update_mouse_clicked
#	check_mouse_collision
#	check_new_click
#
# ================================================================================================

mouse_history = 0
mouse_pressed = 0


# ================================================================================================
#  update_mouse_clicked -- updates the mouse clicks history
#
#      Checks for a new mouse press, and based on that updates the global mouse click history.
#
#  INPUT:  none
#
#  RETURNS:  none
#
#  CREATED: 27/07/2020
# ================================================================================================
def update_mouse_clicked():
    global mouse_history
    global mouse_pressed

    mouse_history = mouse_pressed
    if py.mouse.get_pressed()[0]:
        mouse_pressed = 1
    else:
        mouse_pressed = 0


# ================================================================================================
#  check_mouse_collision -- checks whether or not the cursor is in a hitbox passed in
#
#      Checks whether or not the cursor is inside a rectangle passed in, and returns te result.
#
#  INPUT:  hit_box - tuple - a four-dimensional vector containing the coordinates of the top
#							 left corner of the rect, and the size of the rect.
#
#  RETURNS:  none
#
#  CREATED: 27/07/2020
# ================================================================================================
def check_mouse_collision(hit_box):
    py.event.get()
    mouse_pos = py.mouse.get_pos()
    if hit_box[0] < mouse_pos[0] < hit_box[0] + hit_box[2] and \
            hit_box[1] < mouse_pos[1] < hit_box[1] + hit_box[3]:
        return True
    else:
        return False


# ================================================================================================
#  check_new_click -- checks whether or not a new click has been detected, as of the last update.
#
#      more detailed function description
#
#  INPUT:  none
#
#  RETURNS:  none
#
#  CREATED: 00/00/2020
# ================================================================================================
def check_new_click():
    if py.mouse.get_pressed()[0] and not mouse_pressed:
        return True
    else:
        return False
