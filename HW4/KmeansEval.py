#!/usr/bin/env python
#START STUDENT CODE45
from mrjob.job import MRJob
from mrjob.step import MRStep
from Kmeans import min_distance
import logging, re
import numpy as np

class MRKmeansEval(MRJob):
    
    JOBCONF = {"mapreduce.job.reduces": "1"}
    
    def __init__(self, *args, **kwargs):
        super(MRKmeansEval, self).__init__(*args,**kwargs)
        self.centroids = []
        self.k = 4
    
    def mapper_init(self):        
        self.centroids = [map(float,s.split('\n')[0].split(',')) for s in open("Centroids.txt").readlines()]
    
    def mapper(self, _, line):
        fields = line.split(",")
        cl = fields[1]
        datapoint = (map(float, fields[3:]))
        c_min_idx = min_distance(self.centroids, datapoint)
        yield int(c_min_idx), (int(cl),1)
    
    def reducer(self, key, vals):
        cl_sum = [0]*4
        for cl,n in vals:
            cl_sum[cl] +=n
        yield key, (cl_sum)

if __name__ == '__main__':
    MRKmeansEval.run()