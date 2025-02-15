#!/usr/bin/env python3
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from builtins import int
from builtins import input
from future import standard_library

standard_library.install_aliases()
from chiplotle import *

## HELPER FUNCTIONS ##


def _query_font_size():
    char_height = float(input("font height (in cm)? "))
    char_width = float(input("font width (in cm)? "))
    return char_width, char_height


def _query_pen():
    pen_num = int(input("which pen? "))
    return pen_num


## MAIN FUNCTION ##


def typewriter():
    print("***************************")
    print("* CHIPLOTLE TYPEWRITER!!! *")
    print("***************************")
    print("")

    plotter = instantiate_plotters()[0]

    pen_num = _query_pen()

    set_size = input("set font size (y/N)? ")

    if set_size.lower() == "y":
        cw, ch = _query_font_size()
        plotter.write(SI(cw, ch))

    plotter.select_pen(pen_num)

    print("")
    print("type at the >>> prompt.")
    print("press RETURN after each line to be plotted.")
    print("enter a blank line for options.")
    print("")

    finished = False

    while finished == False:
        line = input(">>> ")
        if len(line) == 0:
            print("(enter): blank line")
            print("p: select new pen")
            print("s: set new font size")
            print("q: quit")
            response = input("command: ")
            if response == "p":
                pen_num = _query_pen()
                plotter.select_pen(pen_num)
            elif response == "s":
                cw, ch = _query_font_size()
                plotter.write(SI(cw, ch))
            elif response == "q":
                finished = True
            else:
                plotter.write(LB("\n\r"))
        else:
            plotter.write(LB(line + "\n\r"))

    print("l8r.")


if __name__ == "__main__":
    typewriter()
