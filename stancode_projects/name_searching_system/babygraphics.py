"""
File: babygraphics.py
Name: Sean Liu
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_coordinate = int(GRAPH_MARGIN_SIZE+((width-GRAPH_MARGIN_SIZE)/len(YEARS))*year_index)
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, (CANVAS_WIDTH - GRAPH_MARGIN_SIZE), GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE), (CANVAS_WIDTH - GRAPH_MARGIN_SIZE),
                       (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE), width=LINE_WIDTH)
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT,
                           width=LINE_WIDTH)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX, (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE), text=YEARS[i],
                           anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    for name in lookup_names:
        ranks = []
        y_coordinates = []
        if name in name_data:
            for i in range(len(YEARS)):
                if str(YEARS[i]) in name_data[name]:
                    ranks.append(name_data[name][str(YEARS[i])])
                    y_coordinates.append(GRAPH_MARGIN_SIZE+((CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)/1000) *
                                         int(name_data[name][str(YEARS[i])]))
                else:
                    # If the name is not on the top-200 list that year, the rank is *.
                    ranks.append('*')
                    y_coordinates.append(CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
        # color_index is used to decide to color of the line.
        color_index = 0
        for i in range(len(lookup_names)):
            if lookup_names[i] == name:
                color_index = i
        # For example, there are 12 years but only 11 lines in-between years are drawn.
        for k in range(len(YEARS)-1):
            canvas.create_line(get_x_coordinate(CANVAS_WIDTH, k), int(y_coordinates[k]),
                               get_x_coordinate(CANVAS_WIDTH, k+1), int(y_coordinates[k+1]), width=LINE_WIDTH,
                               fill=COLORS[color_index % 4])
            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, k)+TEXT_DX, int(y_coordinates[k]),
                               text=f'{name} {ranks[k]}', anchor=tkinter.SW, fill=COLORS[color_index % 4])
            # For the last year, there is no further line but the text needs to be put on.
            if k == len(YEARS)-2:
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, k+1) + TEXT_DX, int(y_coordinates[k+1]),
                                   text=f'{name} {ranks[k+1]}', anchor=tkinter.SW, fill=COLORS[(color_index % 4)])


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
