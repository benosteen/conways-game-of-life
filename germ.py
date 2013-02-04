from conway import *

germ = """
....OO....
.....O....
...O......
..O.OOOO..
..O....O..
.OO.O.....
..O.O.OOOO
O.O.O....O
OO...OOO..
.......OO."""

if __name__ == "__main__":
    play_state(germ, SCALES['HIRAJOSHI'])
    pygame.midi.quit()
