#!/usr/bin/env python
"""
<write your description here>
INPUT:
    <specify record format here>
OUTPUT:
    <specify record format here>
"""
import re
import sys

# read from standard intpu
for line in sys.stdin:
    line = line.strip()
    # tokenize
    words = re.findall(r'[a-z]+', line.lower())
    # emit words and count of 1
    for word in words:
        print '%s\t%s' % (word, 1)