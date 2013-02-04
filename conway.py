import pygame
import pygame.midi

from time import sleep,time

pygame.midi.init()

# 2 corresponds to my USB MIDI output
# 0 is often the default software MIDI
# Trial and Error needed here unfortunately
m = pygame.midi.Output(2)

SCALES = {'CMAJOR': [0,2,4,5,7,9,11],
          'BLUES': [0,3,5,6,7,10,11],
          'MAJORPENT': [0,2,4,7,11],
          'MINORPENT': [0,3,5,7,10],
          'JAZZY': [0,2,4,6,8,10],
          'INSEN': [0,1,5,7,10],
          'HIRAJOSHI': [0,1,5,7,9],
          'THIRDS': [0,4,2,5,4,7,5,9,7,11,13,12],
          'CHROMATIC': [0,1,2,3,4,5,6,7,8,9,10,11]
          }

note_length = 0.2 # 200ms
maxbounds = (32,24) # 32 notes long, 24 (3 octaves) high

# Pick a scale from above or manufacture your own
scale = SCALES['INSEN']

# Notes start at:
offset = 30

# NB cells run from 0 to 31, and 0 to 23

def boundedpoint(old_point):
    return (old_point[0] % maxbounds[0], old_point[1] % maxbounds[1])

def neighbors(cell):
    x, y = cell
    return [boundedpoint((x + 1, y)), boundedpoint((x - 1, y)), 
            boundedpoint((x, y + 1)), boundedpoint((x, y - 1)), 
            boundedpoint((x + 1, y + 1)), boundedpoint((x + 1, y - 1)), 
            boundedpoint((x - 1, y + 1)), boundedpoint((x - 1, y - 1))]

def run(population, generations=100):
    """Runs Conway's game of life on an initial population."""
    population = set(population)
    for i in range(generations):
        population = evolve(population)
    return population


def evolve(population):
    """Evolves the population by one generation."""
    # Get a unique set of discrete cells that need to be checked
    active_cells = population | set([neighbor for p in population
                                    for neighbor in neighbors(p)])
    # For each cell in the set, test if it lives or dies
    new_population = set()
    for cell in active_cells:
        count = sum([neighbor in population for neighbor in neighbors(cell)])
        if count == 3 or (count == 2 and cell in population):
            new_population.add(boundedpoint(cell))
    # Return the new surviving population
    return new_population

def play_midi(notes):
    for cursor in range(maxbounds[0]):
        t = time()
        keys = []
        if notes.has_key(cursor):
            for note in notes[cursor]:
                keys.append(12 * (note / len(scale)) + (scale[note % len(scale)]))
        for k in keys:
            m.note_on(k,100)
        sleep((note_length+t) - time())
        for k in keys:
            m.note_off(k,100)

def vis(pop):
    for i in range(maxbounds[1]):
        line = ""
        for j in range(maxbounds[0]):
            if (j,i) in pop:
                line += "O"
            else:
                line += "."
        print line

def pic_to_set(lifestring):
    i_pop = set()
    y = 0
    for line in lifestring.split("\n"):
        for idx, char in enumerate(line):
            if char == "O":
                i_pop.add((idx,y))
        y += 1
    return i_pop

#glider = set([(0,0), (1,0), (2,0), (0,1), (1,2)])

# See http://www.argentum.freeserve.co.uk/lex.htm
# (Game of Life Lexicon)

beehive_and_dock = """
...OO.
..O..O
...OO.
......
.OOOO.
O....O
OO..OO"""

glider = """
OOO
O..
.O."""

gospel_gun = """
........................O...........
......................O.O...........
............OO......OO............OO
...........O...O....OO............OO
OO........O.....O...OO..............
OO........O...O.OO....O.O...........
..........O.....O.......O...........
...........O...O....................
............OO......................"""


#gameset = pic_to_set(beehive_and_dock)
gameset = pic_to_set(gospel_gun)
#gameset = pic_to_set(glider)

for i in range(200):
    notes = {}
    gameset = evolve(gameset)
    vis(gameset)
    for alivepoint in gameset:
        x,y = alivepoint
        if not notes.has_key(x):
            notes[x] = []
        notes[x].append(y+offset)
    play_midi(notes)
