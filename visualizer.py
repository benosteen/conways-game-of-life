#!/usr/bin/env python
"""

Generates graphics to show traversal paths for linear and convolutive
iteration.

Written by Patrick Fuller, patrickfuller@gmail.com, 19 Nov 12

"""

import Image, ImageDraw
from itertools import product


def draw(cells, image_size=(300, 300), grid_count=10, border_thickness=10):
    """Draws cells onto a grid, returning a PIL image."""
    
    # Get centroid of cells = and place in middle of grid
    x_cent = -sum(cell[0] for cell in cells) / len(cells) + grid_count / 2
    y_cent = -sum(cell[1] for cell in cells) / len(cells) + grid_count / 2
    
    # Initialize a grid with white cells and gray borders
    img = Image.new("RGBA", size=image_size, color=(22,)*3)
    for x, y in product(range(grid_count), repeat=2):
        coords = get_grid_coordinates(x, y, image_size, grid_count,
                                      border_thickness)
        ImageDraw.Draw(img).rectangle(coords, fill=(255,)*3) 
    
    # For each "living" cell, color corresponding cell black
    for x, y in cells:
        coords = get_grid_coordinates(x + x_cent, y + y_cent, image_size,
                                      grid_count, border_thickness)
        # Check if the coordinate is in range. Draw if good, warn otherwise.
        if 0 <= coords[0] < image_size[0] and 0 <= coords[1] < image_size[1]:
            ImageDraw.Draw(img).rectangle(coords, fill=(0,)*3)
        else:
            print "You should increase the grid count of the draw() method!"
    
    return img
        

def get_grid_coordinates(x, y, image_size, grid_count, border_thickness):
    """ Returns (xl, yl, xr, yr) corners corresponding to cell location """
    xl = x * (image_size[0]-border_thickness)/grid_count + border_thickness
    yl = y * (image_size[1]-border_thickness)/grid_count + border_thickness
    xr = (x+1) * (image_size[0]-border_thickness)/grid_count
    yr = (y+1) * (image_size[1]-border_thickness)/grid_count   
    return xl, yl, xr, yr
