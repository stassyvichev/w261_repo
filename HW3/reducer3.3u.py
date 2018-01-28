#!/usr/bin/env python
# START STUDENT CODE HW32CFREQREDUCER
import sys, re
import logging
# initialize trackers
cur_word = None
num_words = 0
# read input key-value pairs from standard input

for line in sys.stdin:
#     logging.warning( line.split("\t"))
    arr = line.split("\t")
    key, count = arr[0], arr[1]
    # tally counts from current key
    if key != cur_word: 
        if cur_word:
            num_words += 1
        cur_word = key
num_words += 1
print '%s' % (num_words)

# END STUDENT CODE HW32CFREQREDUCER