#!/usr/bin/env python
# START STUDENT CODE HW32AMAPPER
import re
import sys

# read from standard input
sys.stderr.write("reporter:counter:mr_count,map,1\n")
for line in sys.stdin:
    line = line.strip()
    # tokenize
    words = re.findall(r"[\w']+", line.lower())
    # emit words and count of 1
    for word in words:
        print '%s\t%s' % (word, 1)
    

# END STUDENT CODE HW32AMAPPER