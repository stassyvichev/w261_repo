#!/usr/bin/env python
"""    
Reducer used for counting words.
INPUT:
    Key-value pairs read from stdin in the form word\tcount 
    for a set of word and all their counts, sorted by key. 
OUTPUT:
    key-value pairs to stdout with each word and its number of counts. 
"""
import sys

# initialize trackers
cur_word = None
cur_count = 0

# read input key-value pairs from standard input
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