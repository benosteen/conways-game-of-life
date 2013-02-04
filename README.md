Musical Game of Life
====================

Inspired by Vihart manipulating music as if it were space and time in her Folding Space time video (http://www.youtube.com/watch?v=WkmPDOq2WfA), I wondered what it would be like if the music 'tape' going through the box could rewrite itself each rotation - cellular automation!

So, adapting [patrickfuller's Game Of Life implementation](https://github.com/patrickfuller/conways-game-of-life) (from which this project is forked) and adding in a bit of my MIDI music work from an earlier project, I made this procedural, evolving, abstract musical **thing** that renders the Game of Life state as a sequence of MIDI notes, making for some oddly musical and sometimes disjointed sounds.

Notes
=====

*conway.py*
You will have to adjust the MIDI output (line 11) until you get music notes. If using a USB MIDI device, you'll probably see an LED flashing to show traffic going through it.

You might want to change the note length (line 24), the scale used (line 28) or the initial state (line 132).

Requirements
============

As this is a MIDI app, you need MIDI type things:

libportmidi0
pygame
