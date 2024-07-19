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

def prob_phred(p, q):
	p = 10 ** -q // 10
	q = -10 * (math.log10(p))
	if 0 < p < 1 and q > 1: return p, q
	
print(prob_phred(.35, q))
print(prob_phred(p, 40))
	