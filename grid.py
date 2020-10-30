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

#
# ------------------------------------------------------------------------------------------------
#
#                                       What the file does.
#
# ------------------------------------------------------------------------------------------------
#
# ================================================================================================
grid_size_pixels = (1000, 600)  # in pixels
grid_size_squares = (500, 300)  # in squares
square_size = (grid_size_pixels[0] / grid_size_squares[0], grid_size_pixels[1] / grid_size_squares[1])

grid = []

for i in range(grid_size_squares[1]):
    grid.append([(255, 255, 255)] * grid_size_squares[0])


def set_colour(location, colour):
    global grid
    try:
        grid[location[1]][location[0]] = colour
    except IndexError:
        pass


def get_colour(location):
    try:
        return grid[location[1]][location[0]]
    except IndexError:
        return 0, 0, 0
