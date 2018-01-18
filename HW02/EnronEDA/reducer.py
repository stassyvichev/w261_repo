#!/usr/bin/env python
"""
Mapper tokenizes and emits words with their class.
INPUT:
    word \t class \t partialCount 
OUTPUT:
    word \t class \t totalCount  
"""
import re
import sys

# initialize trackers
cur_word = None
spam_count, ham_count = 0,0

# read from standard input
for line in sys.stdin:
    # parse input
    word, isSpam, count = line.split('\t')
    
############ YOUR CODE HERE #########
















############ (END) YOUR CODE #########