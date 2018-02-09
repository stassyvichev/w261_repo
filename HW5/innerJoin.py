#!/usr/bin/env python
#START STUDENT CODE44
from mrjob.job import MRJob
from mrjob.step import MRStep
import logging
class MRInnerJoin(MRJob):
    
    SORT_VALUES = True
    JOBCONF = {"mapreduce.job.reduces": "1"}
    def __init__(self, *args, **kwargs):
        super(MRInnerJoin, self).__init__(*args,**kwargs)
        self.countries = {}
        with open("Countries.dat") as file:
            for line in file.readlines():
                fields = line.split("|")
                self.countries[fields[1].replace("\n","")]=fields[0]
        
    def mapper(self, _, line):
        fields = line.split("|")
        if self.countries.get(fields[2]):
            yield fields[0], (fields[1], self.countries.get(fields[2]))
    
    def steps(self):
        return [
            MRStep(mapper = self.mapper)
        ]

if __name__ == "__main__":
    MRInnerJoin.run()