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

class MRsimilarity(MRJob):
  
    def mapper(self, _, line):
        word, stripe = line.split("\t")
        print json.loads(stripe)
  
if __name__ == '__main__':
    MRsimilarity.run()