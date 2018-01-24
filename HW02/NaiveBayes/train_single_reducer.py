#!/usr/bin/env python
"""
Reducer aggregates word counts by class and emits probabilities
with plus one Laplace Smoothing. 

INPUT:
    word \t class \t count
OUTPUT:
    word \t num_c0_class \t num_c1_class \t cond_prob_c0 \t cond_prob_c1
    add ClassPriors record

this reducer should only be used as a single reducer and run with the data from train_reducer_smooth.py reducers, sorted by the first field alphabetically, together with a count file generated that holds the vocab size.  

"""
##################### YOUR CODE HERE ####################
import re
import sys, os

# confirm that we have access to the count file
assert 'p9WordCount.txt' in os.listdir('.'), "ERROR: can't find p9WordCount.txt"
for record in open('p9WordCount.txt', 'rb').readlines():
    vocab_size = record.strip()
    vocab_size = int(vocab_size)-2

# initialize K
K = 1

# read from standard input
for line in sys.stdin:
    # parse input
    
    word, c0_count, c1_count = line.split('\t')
    # print word, isSpam, count
    c0_count = int(c0_count)
    c1_count = int(c1_count)
    # we use * to denote number of documents with specific class
    if word == "*":
        c0_doc_count = c0_count
        c1_doc_count = c1_count
        total_count = c0_doc_count+c1_doc_count
        c0_prior = c0_doc_count/float(total_count)
        c1_prior = c1_doc_count/float(total_count)
        print "%s\t%s,%s,%s,%s" % ("ClassPriors", c0_doc_count, c1_doc_count, c0_prior, c1_prior) 
    elif word == ".":
        # use . to denote count of words with specific class class
        c0_word_count = c0_count
        c1_word_count = c1_count
    else:
        curr_word_c0_count = c0_count
        curr_word_c1_count = c1_count
         
        # calculate probabilities with K and vocab_size
        cond_prob_c0 = (curr_word_c0_count+K)/float(c0_word_count+vocab_size*K)
        cond_prob_c1 = (curr_word_c1_count+K)/float(c1_word_count+vocab_size*K)
        print "%s\t%s,%s,%s,%s" % (word, curr_word_c0_count, curr_word_c1_count,cond_prob_c0 , cond_prob_c1)
        










































##################### (END) CODE HERE ####################