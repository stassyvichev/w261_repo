#!/usr/bin/env python
#START STUDENT CODE45_RUNNER
from KmeansEval import MRKmeansEval
    
mr_job = MRKmeansEval(args=['topUsers_Apr-Jul_2014_1000-words.txt', '--file=Centroids.txt'])
with mr_job.make_runner() as runner:
    runner.run()
    for line in runner.stream_output():
        print mr_job.parse_output_line(line)
#END STUDENT CODE45_RUNNER