#!/usr/bin/env python
#START STUDENT CODE45
from mrjob.job import MRJob
from mrjob.step import MRStep
import logging, re
import numpy as np

def stop_criterion(centroids_old, centroids_new, alpha):
    diff = abs(np.array(centroids_old) - np.array(centroids_new))
    return np.all(diff <= alpha)

def min_distance(centroids, datapoint):
    dp = np.array(datapoint)
    diff = dp -centroids
    diffsq = diff * diff
    minidx = np.argmin(list(diffsq.sum(axis = 1)))
    return minidx

def startCentroidsA(k):
    counter = 0
    centroid_rows = np.random.randint(0,999, size=k)
    centroids = []
    for line in open("topUsers_Apr-Jul_2014_1000-words.txt").readlines():
        if counter in centroid_rows:
            data = re.split(",",line)
            centroids.append([float(d) for d in data[3:]])
        if counter >max(centroid_rows):
            break
        counter +=1
    return centroids

def startCentroidsBC(k):
    counter = 0
    for line in open("topUsers_Apr-Jul_2014_1000-words_summaries.txt").readlines():
        if counter == 1:        
            data = re.split(",",line)
            globalAggregate = [float(data[i+3])/float(data[2]) for i in range(1000)]
        counter += 1
    #perturb the global aggregate for the four initializations    
    centroids = []
    for i in range(k):
        rndpoints = np.random.sample(1000)
        peturpoints = [rndpoints[n]/10+globalAggregate[n] for n in range(1000)]
        centroids.append(peturpoints)
        total = 0
        for j in range(len(centroids[i])):
            total += centroids[i][j]
        for j in range(len(centroids[i])):
            centroids[i][j] = centroids[i][j]/total
    return centroids

def startCentroidsD(k):
    counter = 0
    centroids = [[],[],[],[]]
    for line in open("topUsers_Apr-Jul_2014_1000-words_summaries.txt").readlines():
        if counter in [2,3,4,5]:        
            data = re.split(",",line)
            cls = int(data[1])
            class_agg = [float(d) for d in data[3:]]
            centroids[cls]=class_agg
        counter += 1
    return centroids

class MRKmeans(MRJob):
    
    JOBCONF = {"mapreduce.job.reduces": "1"}
    
    def __init__(self, *args, **kwargs):
        super(MRKmeans, self).__init__(*args,**kwargs)
        self.centroids = []
        self.k = 4
    
    def mapper_init(self):        
        self.centroids = [map(float,s.split('\n')[0].split(',')) for s in open("Centroids.txt").readlines()]
        print len(self.centroids)
    def mapper(self, _, line):
        fields = line.split(",")
        datapoint = (map(float, fields[3:]))
        c_min_idx = min_distance(self.centroids, datapoint)
        yield int(c_min_idx), (datapoint,1)
    
    def reducer(self, c_idx, datapoints):
        total = 0
        num = 0
        for dp,n in datapoints:
            num += n
            total += np.array(dp)
        yield c_idx, (total/num)
    
    def steps(self):
        return [
            MRStep(
                mapper_init= self.mapper_init,
                mapper = self.mapper,
                reducer = self.reducer
            )
        ]
    
if __name__ == '__main__':
    MRKmeans.run()

#END STUDENT CODE45