#!/usr/bin/env python

import re
import sys
from collections import Counter
import json
# read from standard input
sys.stderr.write("reporter:counter:mr_count,map,1\n")
count = 1

for line in sys.stdin:
    line = line.strip().lower()
    words = line.split()
    for word in words:
        pair_counter = Counter()
        for i in xrange(count, len(words)):
            pair_counter[words[i]] +=1
            print '%s\t%s' % ("*",json.dumps({"*":1}))
        if pair_counter:
            print '%s\t%s' % (word, json.dumps(pair_counter))
        count += 1
    count = 1