Musical Game of Life
====================

Inspired by Vihart manipulating music as if it were space and time in her Folding Space time video (http://www.youtube.com/watch?v=WkmPDOq2WfA), I wondered what it would be like if the music 'tape' going through the box could rewrite itself each rotation - cellular automation!

So, adapting [patrickfuller's Game Of Life implementation](https://github.com/patrickfuller/conways-game-of-life) (from which this project is forked) and adding in a bit of my MIDI music work from an earlier project, I made this procedural, evolving, abstract musical **thing** that renders the Game of Life state as a sequence of MIDI notes, making for some oddly musical and sometimes disjointed sounds.

Notes
=====

[conway.py](https://github.com/benosteen/conways-game-of-life/blob/master/conway.py):

You will have to adjust the MIDI output (line 11) until you get music notes. If using a USB MIDI device, you'll probably see an LED flashing to show traffic going through it.

There are example scripts to help you tinker with the outputs:
- [glider_pusher.py](https://github.com/benosteen/conways-game-of-life/blob/master/glider_pusher.py)
- [germ.py](https://github.com/benosteen/conways-game-of-life/blob/master/germ.py)
- [infinite_growth.py](https://github.com/benosteen/conways-game-of-life/blob/master/infinite_growth.py)

The musical scale it can map to are set at the beginning of the [conway.py](https://github.com/benosteen/conways-game-of-life/blob/master/conway.py) file but you can always add in your own. Scales start at zero and each integer increase is a semitone up. For example, the C Major scale (C,D,E,F,G,A,B) is [0,2,4,5,7,9,11].

    ...
    play_state(state, scale = [0,2,4,5,7,9,11], ...)
    ...

Drawing the initial state should also be easy to work out from these examples too!

Requirements
============

As this relies on pygame's midi interface, you'll need that set up. On linux, it's just a case of getting pygame installed.

Key libraries:
- libportmidi0
- pygame
