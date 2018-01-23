#!/usr/bin/env python
"""
Reducer aggregates word counts by class and emits frequencies.

INPUT:
    word \t class \t count
OUTPUT:
    word \t num_c0_class \t num_c1_class \t cond_prob_c0 \t cond_prob_c1
    add ClassPriors record
    
Instructions:
    Again, you are free to design a solution however you see 
    fit as long as your final model meets our required format
    for the inference job we designed in Question 8. Please
    comment your code clearly and concisely.
    
    A few reminders: 
    1) Don't forget to emit Class Priors (with the right key).
    2) In python2: 3/4 = 0 and 3/float(4) = 0.75
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
            total_count = c0_doc_count+c1_doc_count
            print "%s\t%s\t%s\t%s\t%s" % ("ClassPriors", c0_doc_count, c1_doc_count, c0_doc_count/float(total_count), c1_doc_count/float(total_count)) 
            if isSpam:
                c1_word_count += count
            else:
                c0_word_count += count
        elif curr_word !=".":
            cond_prob_c0 = curr_word_c0_count/float(c0_word_count)
            cond_prob_c1 = curr_word_c1_count/float(c1_word_count)
            print "%s\t%s\t%s\t%s\t%s" % (curr_word, curr_word_c0_count, curr_word_c1_count,cond_prob_c0 , cond_prob_c1) 
            curr_word_c0_count = 0
            curr_word_c1_count = 0
            if isSpam == 0:
                curr_word_c0_count += count
            else:
                curr_word_c1_count += count
        curr_word = word
        
            
# printing the last word                
cond_prob_c0 = curr_word_c0_count/float(c0_word_count)
cond_prob_c1 = curr_word_c1_count/float(c1_word_count)
print "%s\t%s\t%s\t%s\t%s" % (curr_word, curr_word_c0_count, curr_word_c1_count,cond_prob_c0 , cond_prob_c1)
##################### (END) CODE HERE ####################