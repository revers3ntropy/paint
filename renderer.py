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
#
# ------------------------------------------------------------------------------------------------
#
#                                       What the file does.
#
# ------------------------------------------------------------------------------------------------
#
# ================================================================================================
screen_x = 1000
screen_y = 600

background_colour = (255, 255, 255)
run_FPS = 60

py.init()

screen = py.display.set_mode((screen_x, screen_y))
clock = py.time.Clock()

screen.fill(background_colour)
py.display.flip()
clock.tick(run_FPS)


def pygame_tick():
    py.display.flip()
    clock.tick(run_FPS)
    screen.fill(background_colour)

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            quit()


def render_grid():
    for row in range(len(grid.grid)):
        for square in range(len(grid.grid[row])):
            square_colour = grid.get_colour((square, row))
            if square_colour != background_colour:
                x_size = (grid.grid_size_pixels[0] / grid.grid_size_squares[0])
                y_size = (grid.grid_size_pixels[1] / grid.grid_size_squares[1])
                x = square * x_size
                y = row * y_size
                rect = (x, y, x_size, y_size)
                py.draw.rect(screen, square_colour, rect)
