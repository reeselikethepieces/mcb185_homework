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
	a = (tp + tn) / (tp + tn + fp + fn) 
	f = 2 * tp/(tp + fp) * tp/(tp + fn) 
	return a,f 
	
print(accuracy_f1(4 , 7, 3, 6))
