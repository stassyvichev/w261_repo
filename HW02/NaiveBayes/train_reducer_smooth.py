#!/usr/bin/env python
"""
Reducer aggregates word counts by class and emits sums
with plus one Laplace Smoothing. Result to be picked up by another reducer. 
INPUT:
    word \t class \t count
OUTPUT:   
    word \t class_0_count \t class_1_count

This reducer takes all the results and aggregates them by first key and classification. The results should be a single file with a row for each word, where values are the number of times the word appears in c=0 documents and the number of times the word appears in c=1 documents. There are two special keys: * signifies that we are counting the classification of documents, . means that we are counting the classification of the total number of words. 
This information is to be passed to a single reducer: train_single_reducer.py

Instructions:
    Start by copying your unsmoothed reducer code
    (including the rest of the docstring info^^).
    Then make the necessary modifications so that you
    perform Laplace plus-k smoothing. See equation 13.7 
    in Manning, Raghavan and Shutze for details.
    
    Although we'll only look at results for K=1 (plus 1)
    smoothing its a good idea to set K as a variable
    at the top of your script so that its easy to change
    if you want to explore the effect of different 'K's.
    
    Please clearly mark the modifications you make to
    implement smoothing with a comment like:
            # LAPLACE MODIFICATION HERE 
"""
##################### YOUR CODE HERE ####################
import re
import sys

# initialize trackers
c0_doc_count, c1_doc_count, c1_word_count, c0_word_count = 0,0,0,0
curr_word = "*"
curr_word_c0_count = 0
curr_word_c1_count = 0

# read from standard input
for line in sys.stdin:
    # parse input
    
    word, isSpam, count = line.split('\t')
    # print word, isSpam, count
    isSpam = int(isSpam)
    count = int(count)
    if curr_word == word:
        # we use * to denote number of documents with specific class
        if word == "*":
            if isSpam:
                c1_doc_count += count
            else:
                c0_doc_count += count
        elif word == ".":
            # use . to denote count of words with specific class class
            if isSpam:
                c1_word_count += count
            else:
                c0_word_count += count
        else:
            # we use -1 to denote word counts
            if isSpam == 0:
                curr_word_c0_count += count
            else:
                curr_word_c1_count += count
    else: 
        if curr_word == "*":
            print "%s\t%s\t%s" % ("*", c0_doc_count, c1_doc_count)
            if isSpam:
                c1_word_count += count
            else:
                c0_word_count += count
        elif curr_word == ".":
            print "%s\t%s\t%s" % (".", c0_word_count, c1_word_count)
            if isSpam == 0:
                curr_word_c0_count += count
            else:
                curr_word_c1_count += count
        else:
            print "%s\t%s\t%s" % (curr_word, curr_word_c0_count, curr_word_c1_count)
            curr_word_c0_count = 0
            curr_word_c1_count = 0
            if isSpam == 0:
                curr_word_c0_count += count
            else:
                curr_word_c1_count += count
        curr_word = word
        
            
# printing the last word                
print "%s\t%s\t%s" % (word, curr_word_c0_count, curr_word_c1_count)










































##################### (END) CODE HERE ####################