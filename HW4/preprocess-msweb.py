#START STUDENT CODE42

import sys
curr_visitor = None
file_name = sys.argv[1]
with open(file_name) as file:
    for line in file.readlines():
        fields = line.split(',')
        if fields[0] =="C":
            curr_visitor = fields[1].replace("\"","")
        elif fields[0] == "V":
            print "V,%s,1,C,%s" % (fields[1],curr_visitor)
#END STUDENT CODE42