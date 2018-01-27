#!/usr/bin/env python
# START STUDENT CODE HW32CFREQMAPPER
import re
import sys

# input here is p32c_results.txt
# read from standard input
for line in sys.stdin:
    line = line.strip()
    word, count = line.split("\t")
    firstLetter = word[0]
    if firstLetter < "m":
        print '%s\t%s\t%s\t' % ("a",word, count)
    else:
        print '%s\t%s\t%s\t' % ("b",word, count)
    
    print '%s\t%s\t%s\t' % ("a",count, 0)
    print '%s\t%s\t%s\t' % ("b",count, 0)
# END STUDENT CODE HW32CFREQMAPPER