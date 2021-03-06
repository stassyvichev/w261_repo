#!/usr/bin/env python
# START STUDENT CODE HW32BMAPPER
import re
import sys

# read from standard input
sys.stderr.write("reporter:counter:mr_count,map,1\n")
for line in sys.stdin:
    line = line.strip()
    if line.split(",")[0] !="Complaint ID":
        issue = line.split(",")[3]
        # tokenize
        words = re.findall(r"[\w']+", issue.lower())
        # emit words and count of 1
        for word in words:
            print '%s\t%s' % (word, 1)

# END STUDENT CODE HW32BMAPPER