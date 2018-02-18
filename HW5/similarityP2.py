#!~/anaconda2/bin/python
# -*- coding: utf-8 -*-
import json
import math
import mrjob
from mrjob.job import MRJob
from mrjob.step import MRStep
import logging

class MRSimilarity(MRJob):
    SORT_VALUES = True
    
    def mapper_first(self, _, line):
        word, stripe = line.split("\t")
        stripe = json.loads(stripe)
        if len(stripe)>1:
            count = 1
            for s in stripe:
                for i in xrange(count, len(stripe)):
                    pair = sorted([s[0], stripe[i][0]])
                    yield pair, s[1]*stripe[i][1]*1.0
                count += 1
            
    
    def reducer_first(self, pair, partSims):
        partSims = list(partSims)
        sum_sims = sum(partSims)
        yield pair, sum_sims
        
    def reducer_second(self, key, value):
        yield key, list(value)
        
    def steps(self):
        return [
            MRStep(
                mapper = self.mapper_first,
                reducer = self.reducer_first,
                jobconf={
                        "mapreduce.job.reduces": "2"
                }
            ),
            MRStep(
                reducer = self.reducer_second,
                jobconf={
                        "mapreduce.job.reduces": "1",
                        "stream.num.map.output.key.fields": 2,
                        "mapreduce.job.output.key.comparator.class" : "org.apache.hadoop.mapred.lib.KeyFieldBasedComparator",
                        "mapreduce.partition.keycomparator.options":"-k2,2nr",
                        "mapred.num.key.comparator.options":"-k2,2nr",
                        "mapred.text.key.comparator.options": "-k2,2nr",
                        "SORT_VALUES":True
                   }
            )
        ]
        
if __name__ == '__main__':
    MRSimilarity.run()