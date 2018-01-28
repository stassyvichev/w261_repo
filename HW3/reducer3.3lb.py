#!/usr/bin/env python
# START STUDENT CODE HW32CFREQREDUCER
import sys, re
import logging
# initialize trackers
biggest_basket = None
most_items = 0
# read input key-value pairs from standard input

for line in sys.stdin:
    logging.warning( line.split("\t"))
    arr = line.split("\t")
    line, count = arr[0], arr[1]
    # tally counts from current key
    if len(line.split("_"))>most_items:
        most_items = len(line.split("_"))
        biggest_basket = line
print '%s\t%s' % (biggest_basket, most_items)