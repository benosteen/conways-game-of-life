#!/usr/bin/env python
"""

Runs Conway's game of life and produces a visualization

"""

import conway
import visualizer

# A starting population (this particular one is called a "glider")
population = set([(0, 0), (1, 0), (2, 0), (0, 1), (1, 2)])

# Number of generations to run
generations = 100

# Iterate and visualize
for i in range(generations):
    visualizer.draw(population).save("conway_%04d.png" % i)
    population = conway.evolve(population)