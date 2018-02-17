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

class MRinvertedIndex(MRJob):
    
    def mapper(self, _, line):
        if line:
            word,stripe = line.split("\t")
            stripe=json.loads(stripe)
            len_dict = len(stripe)
            for key, _ in stripe.items():
                yield key, (word.strip("\""), len_dict)
    
    def reducer(self, key, values):
        yield key, values
        
if __name__ == '__main__':
    MRinvertedIndex.run() 