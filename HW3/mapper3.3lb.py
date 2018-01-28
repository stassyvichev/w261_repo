#!/usr/bin/env python
# START STUDENT CODE HW32CFREQMAPPER
import re
import sys

# read from standard input
basket_count = 0
for line in sys.stdin:
    line = line.strip().lower().replace(" ","_")
    print '%s\t%s' % (line, 1)