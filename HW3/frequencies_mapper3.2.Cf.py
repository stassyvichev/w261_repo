#!/usr/bin/env python
# START STUDENT CODE HW32CFREQMAPPER
import re
import sys

# input here is p32c_results.txt
# read from standard input
for line in sys.stdin:
    line = line.strip()
    word, count = line.split("\t")
    print '%s\t%s\t' % (word, count)
    print '%s\t%s\t' % (count, 0)

# END STUDENT CODE HW32CFREQMAPPER