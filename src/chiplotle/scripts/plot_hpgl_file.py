#!/usr/bin/env python3
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle.tools.plottertools import instantiate_plotters
import sys


def plot_hpgl_file(file):
    """Send an HPGL file to the plotter found connected to the computer."""
    plotter = instantiate_plotters()[0]

    plotter.set_origin_bottom_left()

    plotter.write_file(file)
    ## call flush( ) to wait till all data is written before exiting...
    plotter._serial_port.flush()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Must give HPGL file to plot.\nExample: $ plot_hpgl_file.py myfile.hpgl")
        sys.exit(2)
    file = sys.argv[1]

    plot_hpgl_file(file)
