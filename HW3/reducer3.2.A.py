#!/usr/bin/env python
# START STUDENT CODE HW32AREDUCER
import sys

# initialize trackers
cur_word = None
cur_count = 0

# read input key-value pairs from standard input
sys.stderr.write("reporter:counter:mr_count,reduce,1\n")
for line in sys.stdin:
    key, value = line.split()
    # tally counts from current key
    if key == cur_word: 
        cur_count += int(value)
    # OR emit current total and start a new tally 
    else: 
        if cur_word:
            print '%s\t%s' % (cur_word, cur_count)
        cur_word, cur_count  = key, int(value)

# don't forget the last record! 
print '%s\t%s' % (cur_word, cur_count)
# END STUDENT CODE HW32AREDUCER