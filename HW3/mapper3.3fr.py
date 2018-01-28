#!/usr/bin/env python
# START STUDENT CODE HW32CFREQMAPPER
import re
import sys

# input here is p33c_results.txt
# read from standard input
for line in sys.stdin:
    line = line.strip().lower()
    word, count, prob = line.split("\t")
    if int(count) <50:
        print '%s\t%s\t%s\t%s' % ("A",word, count, prob)
    else:
        print '%s\t%s\t%s\t%s' % ("B",word, count, prob)
    
#     print '%s\t%s\t%s' % ("A",1, 0)
#     print '%s\t%s\t%s' % ("B",1, 0)
# END STUDENT CODE HW32CFREQMAPPER