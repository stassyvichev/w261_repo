#!~/anaconda2/bin/python
# -*- coding: utf-8 -*-
import json
import math
import mrjob
from mrjob.job import MRJob
from mrjob.step import MRStep

class MRSimilarity(MRJob):
    SORT_VALUES = True
    JOBCONF = {"mapreduce.job.reduces": "1"}
    
    def mapper_first(self, _, line):
        word, stripe = line.split("\t")
        stripe = json.loads(stripe)
        if len(stripe)>1:
            count = 1
            for s in stripe:
                for i in xrange(count, len(stripe)):
                    yield (s[0], stripe[i][0]), s[1]*stripe[i][1]*1.0
                count += 1
    
    def reducer_first(self, pair, partSims):
        sum_sims = sum(partSims)
        yield sum_sims, (pair, sum_sims)
        
    def reducer_second(self, key, value):
        yield float(key), list(value)[0]
        
    def steps(self):
        return [
            MRStep(
                mapper = self.mapper_first,
                reducer = self.reducer_first
            ),
            MRStep(
                reducer = self.reducer_second,
                jobconf={
                        "mapreduce.job.reduces": "1",
                        "stream.num.map.output.key.fields": 1,
                        "mapreduce.job.output.key.comparator.class" : "org.apache.hadoop.mapred.lib.KeyFieldBasedComparator",
                        "mapreduce.partition.keycomparator.options":"-k1,1nr",
                        "mapred.num.key.comparator.options":"-k1,1nr",
                        "mapred.text.key.comparator.options": "-k1,1nr",
                        "SORT_VALUES":True
                   }
            )
        ]
        
if __name__ == '__main__':
    MRSimilarity.run()