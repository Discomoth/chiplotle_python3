from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle import __version__
import os


def _run_chiplotle_virtual():
    """The function runs Python, imports Chiplotle and initializes
    a VIRTUAL plotter.
    """
    python_code = []
    python_code.append("print(' ')")
    python_code.append("print('  +-----------------------+')")
    python_code.append("print('  |    Chiplotle! v.%s  |')" % __version__)
    python_code.append("print('  +-----------------------+')")
    python_code.append("print(' ')")
    python_code.append("import sys")
    python_code.append("sys.ps1 = 'chiplotle> '")
    python_code.append("del sys")
    python_code.append("from chiplotle import *")
    python_code.append(
        "from chiplotle.tools.plottertools import instantiate_virtual_plotter"
    )
    python_code.append("plotter = instantiate_virtual_plotter()")

    ##                                            '\n' does now work on Windowz!
    os.system('''python3 -i -c "%s"''' % ";".join(python_code))
