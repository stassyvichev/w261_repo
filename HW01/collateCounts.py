#!/usr/bin/env python
"""
This script reads word counts from STDIN and combines
the counts for any duplicated words.

INPUT & OUTPUT FORMAT:
    word \t count
USAGE:
    python collateCounts.py < yourCountsFile.txt

Instructions:
    For Q6 - Use the provided code as is.
    For Q7 - Delete the section marked "PROVIDED CODE" and replace
             it with your own implementation. Your solution should
             not use a dictionary or store counts in any way - just
             print them as soon as you've added them. HINT: you've
             modified the framework script to ensure that the input
             is alphabetized; how can you use that to your advantage?
"""

# imports
import sys
from collections import defaultdict

########### PROVIDED IMPLEMENTATION ##############
#counts = defaultdict(int)
## stream over lines from Standard Input
#for line in sys.stdin:
#    # extract words & counts
#	word, count  = line.split()
#    # tally counts
#    counts[word] += int(count)
## print counts
#for wrd, count in counts.items():
#    print("{}\t{}".format(wrd,count))
########## (END) PROVIDED IMPLEMENTATION #########

################# YOUR CODE HERE #################
# stream over lines from Standard Input
lastWord = None
tempSum = 0
for line in sys.stdin:
	word, count = line.split()
	if lastWord is None:
		lastWord = word
		tempSum = int(count)
	elif word == lastWord:
		tempSum +=int(count)
	else:
		print("{}\t{}".format(lastWord,tempSum))
		lastWord = word
		tempSum = int(count)
################ (END) YOUR CODE #################
