from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")

class MRWordFreqCount(MRJob):
    
    SORT_VALUES = True

    JOBCONF = {"mapreduce.job.reduces": "1"}
    def __init__(self, *args, **kwargs):
        super(MRWordFreqCount, self).__init__(*args,**kwargs)
    
    def map_max_words(self, _, line):
        word, count = line.split()
        yield word, int(count)
        
    def reduce_max_words(self, word, count):
        yield word, count.next()
        
    def steps(self):
        return [MRStep(mapper = self.map_max_words,
                      reducer = self.reduce_max_words,
                        jobconf={
                        "mapreduce.job.reduces": "1",
                        "stream.num.map.output.key.fields": 2,
                         "mapreduce.job.output.key.comparator.class" : "org.apache.hadoop.mapred.lib.KeyFieldBasedComparator",
                        "mapreduce.partition.keycomparator.options":"-k2,2nr",
                        "mapred.num.key.comparator.options":"-k2,2nr",
#                       "mapred.text.key.comparator.options": "-k2,2nr",
                        "SORT_VALUES":True
                   })
               ]

if __name__ == '__main__':
    MRWordFreqCount.run()