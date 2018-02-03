from mrjob.job import MRJob
from mrjob.step import MRStep
import re
import logging

WORD_RE = re.compile(r"[\w']+")

class MRWordFreqCount(MRJob):
    
    SORT_VALUES = True

    JOBCONF = {"mapreduce.job.reduces": "1"}
    def __init__(self, *args, **kwargs):
        super(MRWordFreqCount, self).__init__(*args,**kwargs)
        
    def init_get_words(self):
        self.words = {}

    def get_words(self, _, line):
        for word in WORD_RE.findall(line):
            word = word.lower()
            self.words.setdefault(word, 0)
            self.words[word] = self.words[word] + 1

    def final_get_words(self):
        for word, val in self.words.iteritems():
            yield word, val
    
    def sum_words(self, word, counts):
        yield word, sum(counts)
    
    def map_max_words(self, word, count):
        logging.warning(word)
        logging.warning(count)
        yield word, int(count)
        
    def reduce_max_words(self, word, count):
        yield word, sum(count)
        
    def steps(self):
        return [MRStep(mapper_init=self.init_get_words,
                       mapper=self.get_words,
                       mapper_final=self.final_get_words,
                       reducer=self.sum_words),
               MRStep(mapper = self.map_max_words,
                      reducer = self.reduce_max_words,
                        jobconf={
                        "mapreduce.job.reduces": "1",
                        "stream.num.map.output.key.fields": 2,
                        "mapreduce.job.output.key.comparator.class" : "org.apache.hadoop.mapred.lib.KeyFieldBasedComparator",
                        "mapreduce.partition.keycomparator.options":"-k2,2nr",
                        "mapred.num.key.comparator.options":"-k2,2nr",
                        "mapred.text.key.comparator.options": "-k2,2nr",
                        "SORT_VALUES":True
                   })
               ]

if __name__ == '__main__':
    MRWordFreqCount.run()