#!/usr/bin/env python
# START STUDENT CODE HW32CFREQMAPPER
import re
import sys

# input here is p32c_results.txt
# read from standard input
for line in sys.stdin:
    line = line.strip().lower()
    words = line.split()
    for word in words:
        if word[0]< "f":
            print '%s\t%s\t%s' % ("A",word, 1)
        else:
            print '%s\t%s\t%s' % ("B",word, 1)
    
    print '%s\t%s\t%s' % ("A",1, 0)
    print '%s\t%s\t%s' % ("B",1, 0)
# END STUDENT CODE HW32CFREQMAPPER