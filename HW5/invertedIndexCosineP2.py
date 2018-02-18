#!~/anaconda2/bin/python
# -*- coding: utf-8 -*-


from __future__ import division
import collections
import re
import json
import math
import numpy as np
import itertools
import mrjob
from mrjob.protocol import RawProtocol
from mrjob.job import MRJob
from mrjob.step import MRStep

class MRinvertedIndexCosine(MRJob):
    SORTED_VALUES = True
    JOBCONF={
#                 "mapreduce.job.reduces": "1",
                "stream.num.map.output.key.fields": 2,
                "mapreduce.job.output.key.comparator.class" : "org.apache.hadoop.mapred.lib.KeyFieldBasedComparator",
                "mapreduce.partition.keycomparator.options":"-k1,1 -k2,2",
                "mapred.num.key.comparator.options":"-k1,1 -k2,2",
                "mapred.text.key.comparator.options": "-k1,1 -k2,2",
                "SORT_VALUES":True
    }
    def mapper(self, _, line):
        word,stripe = line.split("\t")
        stripe=json.loads(stripe)
        stripe_length = 1/math.sqrt(len(stripe))
        for key, _ in stripe.items():
            yield key, (word.strip("\""), stripe_length)
    
    def reducer(self, key, values):
        yield key, list(values)
        
if __name__ == '__main__':
    MRinvertedIndexCosine.run() 