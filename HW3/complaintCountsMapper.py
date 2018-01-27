#!/usr/bin/env python
# START STUDENT CODE HW31MAPPER
import re
import sys

# read from standard input
for line in sys.stdin:
    if line.split(",")[0] != "Complaint ID":
        product = line.split(",")[1].lower()
        if product == "debt collection":
            sys.stderr.write("reporter:counter:product_count,dc,1\n")
            print "%s\t%s" % (product,1)
        elif product =="mortgage":
            sys.stderr.write("reporter:counter:product_count,m,1\n")
            print "%s\t%s" % (product,1)
        else:
            sys.stderr.write("reporter:counter:product_count,o,1\n")
            print "%s\t%s" % ("other",1)
    
# END STUDENT CODE HW31MAPPER