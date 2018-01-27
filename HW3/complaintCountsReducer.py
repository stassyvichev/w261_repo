#!/usr/bin/env python
# START STUDENT CODE HW31REDUCER
import re
import sys

cur_word = None
dc_count, m_count, o_count = 0,0,0
# read from standard input
for line in sys.stdin:
    # parse input
    product, count = line.split('\t')
    if product == cur_word:
        if product == "dc":
            dc_count += int(count)
        elif product == "m":
            m_count += int(count)
        else:
            o_count += int(count)
    else:
        if cur_word:
            if cur_word == "dc":
                print "%s\t%s\t" % (cur_word, dc_count)
            elif cur_word == "m":
                print "%s\t%s\t" % (cur_word, m_count)
            else:
                print "%s\t%s\t" % (cur_word, o_count)
        cur_word = product
        dc_count, m_count, o_count = 0,0,0
        if product == "dc":
            dc_count += int(count)
        elif product == "m":
            m_count += int(count)
        else:
            o_count += int(count)
        
if cur_word == "dc":
    print "%s\t%s\t" % (cur_word, dc_count)
elif cur_word == "m":
    print "%s\t%s\t" % (cur_word, m_count)
else:
    print "%s\t%s\t" % (cur_word, o_count)
# END STUDENT CODE HW31REDUCER