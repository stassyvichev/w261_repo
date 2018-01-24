#!/usr/bin/env python
"""
Reducer to calculate precision and recall as part
of the inference phase of Naive Bayes.
INPUT:
    ID \t true_class \t P(ham|doc) \t P(spam|doc) \t predicted_class
OUTPUT:
    precision \t ##
    recall \t ##
    accuracy \t ##
    F-score \t ##
         
Instructions:
    Complete the missing code to compute these^ four
    evaluation measures for our classification task.
    
    Note: if you have no True Positives you will not 
    be able to compute the F1 score (and maybe not 
    precision/recall). Your code should handle this 
    case appropriately feel free to interpret the 
    "output format" above as a rough suggestion.
"""
import sys

# initialize counters
FP = 0.0 # false positives
FN = 0.0 # false negatives
TP = 0.0 # true positives
TN = 0.0 # true negatives
count = 0.0
correct = 0.0

# read from STDIN
for line in sys.stdin:
    # parse input
    docID, class_, pHam, pSpam, pred = line.split()
    # emit classification results first
    print line[:-2], class_ == pred
    
    # then compute evaluation stats
#################### YOUR CODE HERE ###################
    class_ = int(class_)
    pred = int(pred)
    count +=1
    if class_ == pred:
        correct +=1
    if class_ == 1:
        if pred == 1:
            TP +=1
        else:
            FN +=1
    else:
        if pred == 1:
            FP +=1
        else:
            TN +=1


accuracy = correct/count
if TP != 0.0:
    precision = TP/(TP+FP)
    recall = TP/(TP+FN)
    f_score = 2*(precision*recall)/(precision+recall)
    print "Precision %s " % precision
    print "Recall %s " % recall
    print "Accuracy %s " % accuracy
    print "F-score %s " % f_score
else:
    print "no precision"
    print "no recall"
    print "Accuracy %s " % accuracy
    print "no f-score"
#################### (END) YOUR CODE ###################    