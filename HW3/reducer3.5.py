#!/usr/bin/env python

import sys, re
import logging
import json
from decimal import Decimal
from collections import Counter
# initialize trackers
cur_word = None
cur_counter = Counter()
total_num_pairs = 0
# read input key-value pairs from standard input

sys.stderr.write("reporter:counter:mr_count,reduce,1\n")
for line in sys.stdin:
#     logging.warning( line.split("\t"))
    arr = line.split("\t")
    word, d = arr[0], json.loads(arr[1],parse_float=Decimal)
    if cur_word == word:
        for key,value in d.items():
            cur_counter[key] += value
    else:
        if cur_word:
            if cur_word=="*":
                total_num_pairs = cur_counter["*"]
            for key,value in cur_counter.items():
                if value > 99:
                    pair = sorted([cur_word,key])
                    print '%s\t%s\t%s\t%s' % (pair[0],pair[1], value, value*1.0/total_num_pairs)
        cur_word = word
        cur_counter = Counter(d)
for key,value in cur_counter.items():
    if value > 99:
        pair = sorted([cur_word,key])
        print '%s\t%s\t%s\t%s' % (pair[0],pair[1], value, value*1.0/total_num_pairs)