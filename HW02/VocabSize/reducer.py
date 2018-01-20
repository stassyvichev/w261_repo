#!/usr/bin/env python
"""
reducer to be used to count the number of unique (distinct) words in the supplied files. This accepts key,value pairs from the mapper, recording the number of unique words in the file.
INPUT:
    Key-value pairs read from stdin in the form word\tcount 
    for a set of word and all their counts, sorted by key.
OUTPUT:
    a single count for the number of unique words. 
"""
import re
import sys

cur_word = None
word_count = 1
# read from standard input
for line in sys.stdin:
    line = line.strip()

############ YOUR CODE HERE #########
    # tally counts from current key
    key, value = line.split()
    if key != cur_word: 
        if cur_word:
            word_count +=1
        cur_word = key

# don't forget the last record! 
print word_count 
############ (END) YOUR CODE #########