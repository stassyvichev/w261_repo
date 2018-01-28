#!/usr/bin/env python
# START STUDENT CODE HW32CFREQMAPPER
import re
import sys

# read from standard input
for line in sys.stdin:
    line = line.strip().lower()
    for word in line.split():
        print '%s\t%s' % (word, 1)