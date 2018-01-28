#!/usr/bin/env python
# START STUDENT CODE HW32CFREQREDUCER
import sys, re
import logging
# initialize trackers
cur_word = None
cur_count = 0
total = 0
# read input key-value pairs from standard input

for line in sys.stdin:
#     logging.warning( line.split("\t"))
    arr = line.split("\t")
    extra, key, value = arr[0], arr[1], arr[2]
    if int(value) == 0 and not re.findall(r"[a-z]+", key.lower()):
        total = total + int(key)
    else:
        # tally counts from current key
        if key == cur_word: 
            cur_count += int(value)
        # OR emit current total and start a new tally 
        else: 
            if cur_word:
                prob = (cur_count*1.0)/total
                print '%s\t%s\t%s' % (cur_word, cur_count, prob)
            cur_word, cur_count  = key, int(value)

# don't forget the last record! 
prob = (cur_count*1.0)/total
print '%s\t%s\t%s' % (cur_word, cur_count, prob)

# END STUDENT CODE HW32CFREQREDUCER