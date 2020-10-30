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
import time
import pygame as py
import draw
from colour_selector import ColourSelectManager
from tool_selector import ToolSelectManager
import renderer
#
# ------------------------------------------------------------------------------------------------
#
#                                       What the file does.
#
# ------------------------------------------------------------------------------------------------
#
# ================================================================================================
go = True
tick_number = 0
fps = 1

colour_selector = ColourSelectManager()
tool_selector = ToolSelectManager()


def tick():
    global fps
    global tick_number

    start_time = time.time()

    renderer.render_grid()
    draw.update(not (colour_selector.select or tool_selector.select), colour_selector.current_colour, tool_selector.current_tool, tool_selector.pen, tool_selector.bucket)
    colour_selector.run()

    tool_selector.run()

    renderer.pygame_tick()
    tick_number += 1

    if tick_number % 1 == 0:
        py.display.set_caption(f'FPS: {fps}')

    try:
        fps = round(1 / (time.time() - start_time), 1)
    except ZeroDivisionError:
        fps = 100


def run():
    while go:
        tick()


if __name__ == '__main__':
    run()