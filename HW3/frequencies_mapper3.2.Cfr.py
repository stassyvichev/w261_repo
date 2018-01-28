#!/usr/bin/env python
# START STUDENT CODE HW32CFREQMAPPER
import re
import sys

# input here is p32c_results.txt
# read from standard input
for line in sys.stdin:
    line = line.strip()
    word, count = line.split("\t")
    
    if int(count) < 3000:
        print '%s\t%s\t%s' % ("A",word, count)
    else:
        print '%s\t%s\t%s' % ("B",word, count)
    
    print '%s\t%s\t%s' % ("A",count, 0)
    print '%s\t%s\t%s' % ("B",count, 0)
# END STUDENT CODE HW32CFREQMAPPER