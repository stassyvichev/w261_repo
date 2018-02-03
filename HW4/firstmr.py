from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")


class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        yield "chars", len(line)
        yield "words", len(line.split())
        yield "lines", 1
    
    def reducer_init(self):
        print "reducer init"
    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    MRWordFrequencyCount.run()