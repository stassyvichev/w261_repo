#!/usr/bin/env python

import sys, re
import logging
# initialize trackers
cur_pair = None
cur_count = 0
total_num_pairs = 0
# read input key-value pairs from standard input

sys.stderr.write("reporter:counter:mr_count,reduce,1\n")
for line in sys.stdin:
#     logging.warning( line.split("\t"))
    arr = line.split("\t")
    word1, word2, count = arr[0], arr[1], int(arr[2])
    if (word1,word2) == cur_pair:
        cur_count += count
    else:
        if cur_pair:
            if cur_pair[0]=="*":
                total_num_pairs = cur_count
            if cur_count >99:
                print '%s\t%s\t%s\t%s' % (cur_pair[0],cur_pair[1], cur_count, cur_count*1.0/total_num_pairs)
        cur_pair = (word1,word2)
        cur_count = count
if cur_count > 99:
    print '%s\t%s\t%s\t%s' % (cur_pair[0],cur_pair[1], cur_count, cur_count*1.0/total_num_pairs)