#!/usr/bin/env python
"""
Mapper to be called by Hadoop Streaming for performing word count
INPUT:
    Lines of text passed to stdin, where individual words are specified by spaces. 
    Example:
    the quick brown fox jumped over the lazy dog
OUTPUT:
    Each word encountered in the text, followed by a tab and int(1), printed to stdout. 
    Example:
    the     1
    quick   1
    brown   1
    etc..
"""
import re
import sys

# read from standard input
for line in sys.stdin:
    line = line.strip()
    # tokenize
    words = re.findall(r'[a-z]+', line.lower())
    # emit words and count of 1
    for word in words:
        print '%s\t%s' % (word, 1)