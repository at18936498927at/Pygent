__version__ = "0.1b2"
__author__ = "GitHub at18936498927at"

import sys

if sys.version < (3, 10, 0):
    raise RuntimeError("Your Python's version is a bit low!")
