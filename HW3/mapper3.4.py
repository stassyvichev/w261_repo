#!/usr/bin/env python

import re
import sys

# read from standard input
sys.stderr.write("reporter:counter:mr_count,map,1\n")
count = 1
for line in sys.stdin:
    line = line.strip().lower()
    words = line.split()
    for word in words:
        for i in xrange(count, len(words)):
            pair = sorted([word,words[i]])
            print '%s\t%s\t%s' % (pair[0], pair[1], 1)
            print '%s\t%s\t%s' % ("*","*",1)
        count += 1
    count = 1