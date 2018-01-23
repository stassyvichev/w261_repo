#!/usr/bin/env python
"""
Mapper reads in text documents and emits word counts by class.
INPUT:
    ID \t SPAM \t SUBJECT \t CONTENT \n
OUTPUT:
    word \t class \t count
    
Instructions:
    You know what this script should do, go for it!
    (As a favor to the graders, please comment your code clearly!)
    
    A few reminders:
    1) To make sure your results match ours please be sure
       to use the same tokenizing that we have provided in
       all the other jobs:
         words = re.findall(r'[a-z]+', text-to-tokenize.lower())
         
    2) Don't forget to handle the various "totals" that you need
       for your conditional probabilities and class priors.
"""
##################### YOUR CODE HERE ####################
import re
import sys

# read from standard input
for line in sys.stdin:
    # parse input and tokenize
    docID, _class, subject, body = line.lower().split('\t')
    words = re.findall(r'[a-z]+', subject + ' ' + body) 
    print '%s\t%s\t%s' % ("*", _class, 1)
    for word in words:
        print '%s\t%s\t%s' % (".", _class, 1)
        print '%s\t%s\t%s' % (word, _class, 1)
        print '%s\t%s\t%s' % (word, -1, 1)

##################### (END) YOUR CODE #####################