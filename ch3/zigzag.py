"""
A script printing out a zig zag pattern to the terminal. Hit ctrl-c to exit.
"""

import sys
import time


INDENT = 0  # How many spaces to indent.
INDENT_INCREASING = True  # Whether the indentation is increasing.


try:
    while True:
        print(" " * INDENT, end="")
        print("********")
        time.sleep(0.1)

        if INDENT_INCREASING:
            INDENT = INDENT + 1
            if INDENT == 20:
                INDENT_INCREASING = False
        else:
            INDENT = INDENT - 1
            if INDENT == 0:
                INDENT_INCREASING = True

except KeyboardInterrupt:
    sys.exit()
