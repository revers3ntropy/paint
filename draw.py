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
import pygame as py
import grid
import renderer
#
# ------------------------------------------------------------------------------------------------
#
#                                       What the file does.
#
# ------------------------------------------------------------------------------------------------
#
# ================================================================================================

mouse_down_history = False
mouse_last_position = (0, 0)

slow_fill = False


def screen_space_to_grid(pos):
    pos = list(pos)
    for i in range(2):
        pos[i] /= grid.grid_size_pixels[i] / grid.grid_size_squares[i]
        pos[i] = round(pos[i])

    return pos


# takes in two corners of the rect
def draw_rect_screen_space(a, b, colour):
    a = screen_space_to_grid(a)
    b = screen_space_to_grid(b)

    if a[0] > b[0]:
        max_x = a[0]
        min_x = b[0]
    else:
        max_x = b[0]
        min_x = a[0]

    if a[1] > b[1]:
        max_y = a[1]
        min_y = b[1]
    else:
        max_y = b[1]
        min_y = a[1]

    for x in range(min_x, max_x):
        for y in range(min_y, max_y):

            grid.set_colour((x, y), colour)


def draw_line_screen_space(a, b, colour):
    a = screen_space_to_grid(a)
    b = screen_space_to_grid(b)

    if b[0] < a[0]:
        b, a = a, b

    x0 = a[0]
    y0 = a[1]
    x1 = b[0]
    y1 = b[1]

    dx = abs(x1-x0)

    if x0 < x1:
        sx = 1
    else:
        sx = -1

    dy = -abs(y1-y0)

    if y0 < y1:
        sy = 1
    else:
        sy = -1

    err = dx + dy  # error value e_xy #
    while True:
        grid.set_colour((x0, y0), colour)
        if x0 == x1 and y0 == y1:
            return False

        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x0 += sx

        if e2 <= dx:
            err += dx
            y0 += sy


def correct_for_frames(current_colour):
    draw_line_screen_space(mouse_last_position, py.mouse.get_pos(), current_colour)


def draw(pos, current_colour):
    if mouse_down_history:
        correct_for_frames(current_colour)
    else:
        grid.set_colour(screen_space_to_grid(pos), current_colour)


def update(should_draw, current_colour, current_tool, pen, bucket):
    global mouse_last_position
    global mouse_down_history

    if py.mouse.get_pressed()[0] and should_draw:

        pos = list(py.mouse.get_pos())

        if current_tool == pen:
            draw(pos, current_colour)
        elif current_tool == bucket:
            fill_from(screen_space_to_grid(pos), current_colour)

        mouse_last_position = pos
        mouse_down_history = True

    else:
        mouse_down_history = False


def fill_from(point, current_colour):

    queue = [point]

    while queue:
        if slow_fill:
            renderer.render_grid()
            renderer.pygame_tick()

        directions = {
            0: (0, 1),
            1: (1, 0),
            2: (0, -1),
            3: (-1, 0)
        }

        for i in range(4):
            check_point = (queue[0][0] + directions[i][0], queue[0][1] + directions[i][1])
            check_colour = grid.get_colour(queue[0])

            if check_colour == grid.get_colour(check_point) and grid.get_colour(check_point) != current_colour:
                queue.append(check_point)

        grid.set_colour(queue[0], current_colour)
        queue.pop(0)
