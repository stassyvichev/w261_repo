from mrjob.job import MRJob
from mrjob.step import MRStep

class MrJobLRBatchGD(MRJob):
    def get_weights(self):
        with open("weights.txt", "r") as f:
            self.weights = [float(v) for v in f.readline().split(",")]
        self.partial_gradient = [0]*len(self.weights)
        self.partial_count = 0
    