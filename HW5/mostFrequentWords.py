#!~/anaconda2/bin/python
# -*- coding: utf-8 -*-

import re

import mrjob
from mrjob.protocol import RawProtocol
from mrjob.job import MRJob
from mrjob.step import MRStep

class mostFrequentWords(MRJob):
 
    def mapper(self, _, line):
        fields = line.strip("\n").split("\t")
        count = int(fields[1])
        for word in fields[0].split(" "):
            yield word.lower(), count
    
    def reducer(self, key, values):
        yield key, sum(values)
        
        
if __name__ == '__main__':
    mostFrequentWords.run()