"""
write fxn that converts probabilities --> PHRED scores adn vice-versa
input parameters, x: 0 < x < 1 
return PHRED scores

for x > 1 
return probabilities 

values 0 and 1 are not permitted

pseudo 
def name(p, q):
	if given value for p: return formula 
	elif given value for q: return formula 
	else: return 
print(name(value, q))
print(name(p, value)) 
"""
# x is prob; y is phred 

import math

def prob_phred(x):
	if x > 0 and x < 1: return -10 * (math.log10(x)) 
	return 10 ** (-x / 10)
	
print(prob_phred(.35))	# guess these are not good examples for phred scores 
print(prob_phred(.68))  # "" 
print(prob_phred(.95))
print(prob_phred(.97))
print(prob_phred(.99))
print(prob_phred(.01))
print(prob_phred(.12))
print(prob_phred(10))
print(prob_phred(40))
print(prob_phred(60))
	
	