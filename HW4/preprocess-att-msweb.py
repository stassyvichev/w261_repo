#START STUDENT CODE42

import sys
curr_visitor = None
file_name = sys.argv[1]
with open(file_name) as file:
    for line in file.readlines():
        fields = line.split(',')
        if fields[0] =="A":
            print "%s,%s" % (fields[1],fields[4].replace("\"","").replace("\n",""))
#END STUDENT CODE42