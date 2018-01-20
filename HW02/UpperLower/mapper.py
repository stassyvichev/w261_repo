#!/usr/bin/env python
"""
mapper that processes lines passed to it in stdin to produce a k-v pair for each word in the form of (upper,1) if the word is upper case and (lower,1) otherwise. 
INPUT:
    Lines of text passed to stdin, where individual words are separated by spaces. 
    Example:
    The quick Brown fox jumped over the lazy dog
OUTPUT:
    The case of each word encountered in the text, followed by a tab and int(1), printed to stdout. 
    Example:
    upper     1
    lower   1
    upper   1
    etc..
"""
import re
import sys

# read from standard input
for line in sys.stdin:
    line = line.strip()
    
    ############ YOUR CODE HERE #########
    # tokenize
    words = re.findall(r'[a-zA-Z]+', line)
    # emit case of words and count of 1
    for word in words:
        if word[0]==word[0].lower():
            print '%s\t%s' % ("lower", 1)
        else:
            print '%s\t%s' % ("upper", 1)
    ############ (END) YOUR CODE #########