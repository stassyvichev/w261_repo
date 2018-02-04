#!/usr/bin/env python
#START STUDENT CODE45_RUNNER
from Kmeans import MRKmeans, stop_criterion, startCentroidsA, startCentroidsBC, startCentroidsD
k = 4
alpha = 0.01
centroids = startCentroidsD(k)
with open('Centroids.txt', 'w+') as f:
    f.writelines(','.join(str(j) for j in i) + '\n' for i in centroids)
    
mr_job = MRKmeans(args=['topUsers_Apr-Jul_2014_1000-words.txt', '--file=Centroids.txt'])

i = 0
while(1):
    centroids_old = centroids[:]
    print "iteration "+str(i)
    with mr_job.make_runner() as runner:
        runner.run()
        for line in runner.stream_output():
            c_idx, centroid_loc = mr_job.parse_output_line(line)
            print c_idx, len(centroid_loc)
            centroids[c_idx] = centroid_loc
        # Update the centroids for the next iteration
        with open('Centroids.txt', 'w') as f:
            f.writelines(','.join(str(j) for j in i) + '\n' for i in centroids)
        
    print "\n"
    i = i + 1
    if(stop_criterion(centroids_old,centroids,alpha)):
        break
print "Centroids\n"
#END STUDENT CODE45_RUNNER