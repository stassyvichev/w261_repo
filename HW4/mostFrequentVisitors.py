#!/usr/bin/env python
#START STUDENT CODE44
from mrjob.job import MRJob
from mrjob.step import MRStep
import logging
class MRVisitorCount(MRJob):
    
    SORT_VALUES = True
    JOBCONF = {"mapreduce.job.reduces": "1"}
    def __init__(self, *args, **kwargs):
        super(MRVisitorCount, self).__init__(*args,**kwargs)
        
    def mapper_visits(self, _, line):
        fields = line.split(",")
#         if len(fields) == 5:
#             yield (fields[1],"C",fields[4]),1
#         elif len(fields) == 2:
#             yield (fields[0],"A",fields[1]),1
        if len(fields) == 5:
            yield int(fields[1]), ("C",fields[4], 1)
        elif len(fields) == 2:
            yield int(fields[0]), ("A",fields[1], 1)

    def reducer_visits(self, page_id, visits):
        visits = list(visits)
        logging.warning(page_id)
        logging.warning(visits)
        page_path = None
        curr_cust = None
        curr_count = 0
        max_cust = None
        max_count = 0
        for val in visits:
            if val[0] == "A":
                page_path = val[1]
            elif curr_cust == val[1]:
                curr_count +=val[2]
            else:
                if curr_cust:
                    if curr_count > max_count:
                        max_cust = curr_cust
                        max_count = curr_count
                curr_cust = val[1]
                curr_count = val[2]
        if curr_count > max_count:
            max_cust = curr_cust
            max_count = curr_count
        logging.warning( "end for "+str(page_id))
        yield page_path, (page_id, max_cust, max_count)
    
    def steps(self):
        return [
            MRStep(mapper = self.mapper_visits,
                   reducer = self.reducer_visits,
                   jobconf={
                       "mapreduce.job.reduces": "1",
                       "stream.num.map.output.key.fields": 3,
                       "mapreduce.job.output.key.comparator.class" : "org.apache.hadoop.mapred.lib.KeyFieldBasedComparator",
                       "mapreduce.partition.keycomparator.options":"-k1,1 -k2,2 -k3,3n",
                       "SORT_VALUES":True
                   }
                  )
        ]
if __name__ == "__main__":
    MRVisitorCount.run()
#END STUDENT CODE44