from mrjob.job import MRJob
from mrjob.step import MRStep
import numpy as np

def generate_random_weights():
    weights = np.array([random.uniform(-3,3),random.uniform(-3,3)])
#     print weights
    # Write the weights to the files
    with open('weights.txt', 'w+') as f:
        f.writelines(','.join(str(j) for j in weights)) 
    return weights

class MrJobLRBatchGD(MRJob):
    def get_weights(self):
        with open("weights.txt", "r") as f:
            self.weights = [float(v) for v in f.readline().split(",")]
        self.partial_gradient = [0.0]*len(self.weights)
        self.partial_gradient = np.array(self.partial_gradient)
        self.partial_count = 0
    
    def mapper(self, _, line):
        y,x = line.split(",")
        x = np.array([1,float(x)])
        y = float(y)
        w = np.array(self.weights)
        gdnt = np.dot(y- np.dot(x,w),x)
#         self.partial_gradient = [self.partial_gradient[0]+ gdnt[0], self.partial_gradient[1]+ gdnt[1]]
        self.partial_gradient += gdnt
        self.partial_count +=1
#         yield ((y- x*w)*x,1)
    
    def mapper_final(self):
        yield None, (self.partial_gradient, self.partial_count)
    
    
    def reducer(self, _, gradients_counts):
        final_gradient = np.array([0.0]*2)
        final_count = 0
        for pg, pc in gradients_counts:
            final_count +=pc
            final_gradient += pg
        yield None, [final_gradient/final_count]
    
    
    def steps(self):
        return [
            MRStep(
                mapper_init = self.get_weights,
                mapper = self.mapper,
                mapper_final = self.mapper_final,
                reducer = self.reducer
            )
        ]

if __name__ == '__main__':
    MrJobLRBatchGD.run()