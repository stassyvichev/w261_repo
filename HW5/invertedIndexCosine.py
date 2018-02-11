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
    
    def mapper(self, _, line):
        if line:
            word,stripe = line.split()
            stripe=json.loads(stripe)
            stripe_length = 1/math.sqrt(len(stripe))
            for key, _ in stripe.items():
                yield key, (word.strip("\""), stripe_length)
    
    def reducer(self, key, values):
        yield key, values
        
if __name__ == '__main__':
    MRinvertedIndexCosine.run() 