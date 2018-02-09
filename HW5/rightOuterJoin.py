#!/usr/bin/env python
#START STUDENT CODE44
from mrjob.job import MRJob
from mrjob.step import MRStep
import logging
class MRRightOuterJoin(MRJob):
    
    SORT_VALUES = True
    JOBCONF = {"mapreduce.job.reduces": "1"}
    def __init__(self, *args, **kwargs):
        super(MRRightOuterJoin, self).__init__(*args,**kwargs)
        self.countries = {}
        with open("Countries.dat") as file:
            for line in file.readlines():
                fields = line.split("|")
                self.countries[fields[1].replace("\n","")]=fields[0]
    
    def mapper(self, _, line):
        fields = line.split("|")
        if self.countries.get(fields[2]):
            yield self.countries.get(fields[2]), (fields[1], fields[0])
    
    def reducer_init(self):
        self.countries_done = []   
    
    def reducer_final(self):
        for key, value in self.countries.items():
            if value not in self.countries_done:
                yield value, None
    
    def reducer(self, key, value):
        if key in self.countries.values():
            self.countries_done.append(key)
        for v in value:
            yield key, v
            
    def steps(self):
        return [
            MRStep(mapper = self.mapper,
                   reducer = self.reducer,
                   reducer_init = self.reducer_init,
                   reducer_final = self.reducer_final)
        ]
if __name__ == "__main__":
    MRRightOuterJoin.run()