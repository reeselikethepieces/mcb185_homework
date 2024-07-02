"""
pseudo code
	true positives, false positives, true negatives, and false negatives 
	write fxn returns accuracy and F1 score 

	1. def fxn(a, f):
		print(a, f)
	2. F1 scores are between 0-1 so this will have to be a conditional statement
	
help from internet
	Precision = T+/(T+ + F+)
	recall= T+/(T+ + F-) 
		F1 = 2 * precision * recall / (precision + recall)  
"""

def accuracy_f1(tp, fp, fn, tn):
	p = tp / (tp + fp)
	r = tp / (tp + fn)
	f <= 1 and >= 0:
	
	if tp  or  tn: return (tp + tn) / (tp + tn + fp + fn), 2 * p * r 
	elif fp:         return 'type I error'
	else fn:         return 'type II error' 

print(accuracy_f1(4 , 7, 3, 6))
