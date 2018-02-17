#!~/anaconda2/bin/python
# -*- coding: utf-8 -*-

import re

import mrjob
from mrjob.protocol import RawProtocol
from mrjob.job import MRJob
from mrjob.step import MRStep

class longest5gram(MRJob):
#     SORT_VALUES = True
    def mapper(self, _, line):
        fields = line.strip("\n").split("\t")
        yield len(fields[0]), fields[0]
    
    def reducer_init(self):
        self.longest_ngrams = None
        self.longest_size = 0
        
    def reducer(self, key, values):
        if int(key)> self.longest_size:
            self.longest_size = int(key)
            self.longest_ngrams = list(values)
            
    def reducer_final(self):
        yield self.longest_size, ";".join(list(self.longest_ngrams))
    
    def reducer_2_init(self):
        self.longest_2_ngrams = None
        self.longest_2_size = 0
    
    def reducer_2(self, key, values):
        if int(key)> self.longest_2_size:
            self.longest_2_size = int(key)
            self.longest_2_ngrams = values
        elif int(key) == self.longest_2_size:
            self.longest_2_ngrams = list(self.longest_2_ngrams)+list(values)
            
    def reducer_2_final(self):
        yield self.longest_2_size, ";".join(list(self.longest_2_ngrams))
        
    def steps(self):
        return [
            MRStep(
                mapper = self.mapper,
                reducer_init = self.reducer_init,
                reducer_final = self.reducer_final,
                reducer = self.reducer,
                jobconf={
                    "mapreduce.job.reduces": "2",
                    "stream.num.map.output.key.fields": 1,
                    "mapreduce.job.output.key.comparator.class" : "org.apache.hadoop.mapred.lib.KeyFieldBasedComparator",
                    "mapreduce.partition.keycomparator.options":"-k1,1nr",
                }
#                 jobconf={
#                     "stream.num.map.output.key.fields": 1,
#                     "mapreduce.job.output.key.comparator.class" : "org.apache.hadoop.mapred.lib.KeyFieldBasedComparator",
#                     "mapreduce.partition.keycomparator.options":"-k1,1nr",
#                     "mapred.num.key.comparator.options":"-k1,1nr",
#                     "mapred.text.key.comparator.options": "-k1,1nr",
#                     "SORT_VALUES":True
#                 }
            ),
            MRStep(
                reducer_init = self.reducer_2_init,
                reducer_final = self.reducer_2_final,
                reducer = self.reducer_2,
                jobconf={
                    "mapreduce.job.reduces": "1"
                }
            )
        ]
    
if __name__ == '__main__':
    longest5gram.run()