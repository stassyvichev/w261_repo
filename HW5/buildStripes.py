#!~/anaconda2/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
import re
import mrjob
import json
from mrjob.protocol import RawProtocol
from mrjob.job import MRJob
from mrjob.step import MRStep

class MRbuildStripes(MRJob):
    SORT_VALUES = True
    JOBCONF = {"mapreduce.job.reduces": "1"}
    
    def mapper(self, _, line):
        fields = line.lower().strip("\n").split("\t")
        words = fields[0].split(" ")
        occurrence_count = int(fields[1])
        count = 1
        for word in words:
            for i in xrange(count, len(words)):
                yield word, (words[i], occurrence_count)
                yield words[i], (word, occurrence_count)
            count += 1
    
    def reducer_init(self):
        print
        
    def reducer(self, word, occurrence_counts):
        stripe = {}
        for other_word, occurrence_count in occurrence_counts:
            stripe[other_word] = stripe.get(other_word,0)+occurrence_count
        yield word, stripe

if __name__ == '__main__':
    MRbuildStripes.run()