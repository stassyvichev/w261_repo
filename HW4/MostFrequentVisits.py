#!/usr/bin/env python
#START STUDENT CODE43
from mrjob.job import MRJob
from mrjob.step import MRStep

class MRPageCount(MRJob):
    
    
    def __init__(self, *args, **kwargs):
        super(MRPageCount, self).__init__(*args,**kwargs)
#         self.JOBCONF = {
#                "stream.num.map.output.key.fields": "2",
#                "stream.map.output.field.separator":",",
#                'mapred.output.key.comparator.class':'org.apache.hadoop.mapred.lib.KeyFieldBasedComparator',
#                'mapred.text.key.comparator.options': '-k2,2nr',
#                    }
#         self.SORT_VALUES = False
        
    def mapper_pages(self, _, line):
        fields = line.split(",")
        yield fields[1], int(fields[2])

    def reducer_pages(self, page, visits):
#         yield None, (sum(visits), page)
        yield page, sum(visits)
    
#     def reducer_find_most_freq_pages(self, _,page_freq_pairs):
#         for pair in sorted(page_freq_pairs, reverse=True)[:5]:
#             yield pair
    def reducer_find_most_freq_pages(self, page, count):
        yield page, count
            
    def steps(self):
        return [
            MRStep(mapper = self.mapper_pages,
                  reducer = self.reducer_pages),
            MRStep(
                reducer = self.reducer_find_most_freq_pages, 
#                    jobconf={
#                        "stream.num.map.output.key.fields": "2",
#                        "stream.map.output.field.separator":",",
#                        'mapred.output.key.comparator.class':'org.apache.hadoop.mapred.lib.KeyFieldBasedComparator',
#                        'mapred.text.key.comparator.options': '-k2,2nr',
# #                        "SORT_VALUES":True
#                    }
            )
        ]
if __name__ == "__main__":
    MRPageCount.run()
#END STUDENT CODE43