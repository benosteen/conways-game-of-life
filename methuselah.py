from conway import *

#Paul Callahan found, in November 1997, two 10-cell patterns with infinite growth
# Infinite growth
# http://www.argentum.freeserve.co.uk/lex_i.htm

offset = 30

state = """
.............
..........OO.
.......O.O...
.......O.....
.......O.O...
.............
"""

if __name__ == "__main__":
#    play_and_render(state, SCALES['MINORPENT'], cycles = 200, offset = offset)
    play_state(state, SCALES['MINORPENT'], cycles = 200, offset = offset)
    pygame.midi.quit()
