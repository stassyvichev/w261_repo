from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")

class MRWordFreqCount(MRJob):
    
    SORT_VALUES = False

    JOBCONF = {
                "mapreduce.job.reduces": "1",
                       "stream.num.map.output.key.fields": "1",
                       'mapred.text.key.comparator.options': '-k1,1nr',
    }
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
#         yield None, (word, sum(counts))
        v = sum(counts)
        yield v, word

    
    def map_max_words(self, word, count):
#         print "m",word, count
        yield word, int(count)
        
    def reduce_max_words(self, count, word):
        yield word, count
        
    def steps(self):
        return [MRStep(mapper_init=self.init_get_words,
                       mapper=self.get_words,
                       mapper_final=self.final_get_words,
                       reducer=self.sum_words),
               MRStep(reducer = self.reduce_max_words,
                     jobconf={
                       "mapreduce.job.reduces": "2",
                       'mapred.text.key.comparator.options': '-k1,1nr',
                       "SORT_VALUES":True
                   })
               ]

if __name__ == '__main__':
    MRWordFreqCount.run()