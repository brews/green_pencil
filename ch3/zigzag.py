"""
A script printing out a zig zag pattern to the terminal. Hit ctrl-c to exit.
"""

import time
import sys


INDENT = 0  # How many spaces to indent.
INDENT_INCREASING = True  # Whether the indentation is increasing or not.


try:
    while True:  # The main program loop.
        print(" " * INDENT, end="")
        print("********")
        time.sleep(0.1)  # Pause for 1/10 of a second.

        if INDENT_INCREASING:
            # Increase the number of spaces:
            INDENT = INDENT + 1
            if INDENT == 20:
                # Change direction:
                INDENT_INCREASING = False

        else:
            # Decrease the number of spaces:
            INDENT = INDENT - 1
            if INDENT == 0:
                # Change direction:
                INDENT_INCREASING = True
except KeyboardInterrupt:
    sys.exit()
