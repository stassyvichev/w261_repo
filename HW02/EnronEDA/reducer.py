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
    if word == cur_word:
        if int(isSpam):
            spam_count += int(count)
        else:
            ham_count += int(count)
    else:
        if cur_word:
            print "%s\t%s\t%s\t" % (cur_word, 0, ham_count)
            print "%s\t%s\t%s\t" % (cur_word, 1, spam_count)
        cur_word = word
        spam_count, ham_count = 0,0
        if int(isSpam):
            spam_count += int(count)
        else:
            ham_count += int(count)
        
print "%s\t%s\t%s\t" % (cur_word, 0, ham_count)
print "%s\t%s\t%s\t" % (cur_word, 1, spam_count)
############ (END) YOUR CODE #########